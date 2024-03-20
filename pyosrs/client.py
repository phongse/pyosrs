import asyncio
from typing import Dict, Tuple

import httpx
from httpx import Response

from .enums import (
    BOSSES_INDEX,
    CLUES_INDEX,
    GAME_MODE,
    MINIGAMES_INDEX,
    SKILLS_INDEX,
)
from .exceptions import InvalidAPIResponseException, InvalidUserException
from .models import Bosses, Clues, Hiscore, Minigame, Minigames, Skill, Skills
from .utils import calc_combat_level


class Pyosrs:
    def __init__(self):
        self.session = httpx.AsyncClient(
            base_url="https://secure.runescape.com/",
            timeout=5.0,
        )

    async def __aenter__(self):
        await self.session.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.__aexit__(exc_type, exc, tb)

    async def _get_hiscore(
        self, username: str, game_mode: GAME_MODE = GAME_MODE.MAIN
    ) -> httpx.Response:
        response = await self.session.get(
            f"m={game_mode.value}/index_lite.json?player={username}"
        )
        response.raise_for_status()
        return response

    async def get_hiscore(
        self, username: str, game_mode: GAME_MODE = GAME_MODE.MAIN
    ) -> Hiscore:
        """
        Retrieves the hiscore for a given user and game mode.

        Args:
            username (str): The username of the player to retrieve hiscore for.
            game_mode (GAME_MODE, optional): The game mode to retrieve hiscore
            for. Defaults to GAME_MODE.MAIN.

        Returns:
            Hiscore: The parsed hiscore data for the given username and game mode.

        Raises:
            InvalidUserException: If the given username is invalid.
            InvalidAPIResponseException: If there is a new type of hiscore data
            response that hasn't been accounted for.
        """

        try:
            response: Response = await self._get_hiscore(username, game_mode)
        except httpx.HTTPStatusError:
            raise InvalidUserException(username)

        skills: Dict[str, Skill] = {}
        minigames: Dict[str, Minigame] = {}
        clues: Dict[str, Minigame] = {}
        bosses: Dict[str, Minigame] = {}

        json_response = response.json()
        skills_response = json_response.get("skills")
        activities_response = json_response.get("activities")

        for skill in skills_response:
            if skill["id"] in SKILLS_INDEX:
                skills[SKILLS_INDEX[skill["id"]][0]] = Skill(
                    rank=skill["rank"],
                    level=skill["level"],
                    experience=skill["xp"],
                )

        for activity in activities_response:
            if activity["id"] in MINIGAMES_INDEX:
                minigames[MINIGAMES_INDEX[activity["id"]][0]] = Minigame(
                    rank=activity["rank"],
                    score=activity["score"],
                )
            elif activity["id"] in CLUES_INDEX:
                clues[CLUES_INDEX[activity["id"]][0]] = Minigame(
                    rank=activity["rank"],
                    score=activity["score"],
                )
            elif activity["id"] in BOSSES_INDEX:
                bosses[BOSSES_INDEX[activity["id"]][0]] = Minigame(
                    rank=activity["rank"],
                    score=activity["score"],
                )
            else:
                raise InvalidAPIResponseException()

        combat_level = calc_combat_level(
            defence=skills["defence"].level,
            hitpoints=skills["hitpoints"].level,
            prayer=skills["prayer"].level,
            attack=skills["attack"].level,
            strength=skills["strength"].level,
            ranged=skills["ranged"].level,
            magic=skills["magic"].level,
        )

        return Hiscore(
            username=username,
            game_mode=game_mode,
            combat_level=combat_level,
            skills=Skills(**skills),
            minigames=Minigames(**minigames),
            clues=Clues(**clues),
            bosses=Bosses(**bosses),
        )

    async def get_game_mode(self, username: str) -> Tuple[GAME_MODE, Hiscore]:
        """
        Determines the game mode of a given username by comparing the experience
        levels across different modes using the hiscore API.

        Args:
            username (str): The username to search.

        Returns:
            A tuple containing the game mode and the corresponding Hiscore object
            representing the player's stats in that mode. The game mode can be one
            of the following:

            - GAME_MODE.MAIN: Main mode
            - GAME_MODE.IRONMAN: Ironman mode
            - GAME_MODE.HARDCORE: Hardcore mode
            - GAME_MODE.ULTIMATE: Ultimate mode

        Raises:
            InvalidUserException: If the hiscore API returns an error or no
            hiscore data is found for the given username.
        """

        game_modes = [
            GAME_MODE.MAIN,
            GAME_MODE.IRONMAN,
            GAME_MODE.HARDCORE,
            GAME_MODE.ULTIMATE,
        ]
        tasks = [
            asyncio.create_task(self.get_hiscore(username, game_mode))
            for game_mode in game_modes
        ]
        hiscores = {}
        for task in asyncio.as_completed(tasks):
            try:
                hiscore = await asyncio.shield(task)
                hiscores[hiscore.game_mode] = hiscore
            except:  # noqa: E722
                pass

        if not hiscores:
            raise InvalidUserException(username)

        if GAME_MODE.MAIN in hiscores:
            if GAME_MODE.IRONMAN not in hiscores or (
                GAME_MODE.IRONMAN in hiscores
                and hiscores[GAME_MODE.IRONMAN].skills.overall.experience
                < hiscores[GAME_MODE.MAIN].skills.overall.experience
            ):
                return GAME_MODE.MAIN, hiscores[GAME_MODE.MAIN]

        # We want to ensure that the user has an ironman hiscore entry
        # in case they don't meet the requirements to be on the main hiscore
        if GAME_MODE.IRONMAN not in hiscores:
            raise InvalidUserException(username)

        if (
            GAME_MODE.HARDCORE in hiscores
            and hiscores[GAME_MODE.HARDCORE].skills.overall.experience
            >= hiscores[GAME_MODE.IRONMAN].skills.overall.experience
        ):
            return GAME_MODE.HARDCORE, hiscores[GAME_MODE.HARDCORE]
        elif (
            GAME_MODE.ULTIMATE in hiscores
            and hiscores[GAME_MODE.ULTIMATE].skills.overall.experience
            >= hiscores[GAME_MODE.IRONMAN].skills.overall.experience
        ):
            return GAME_MODE.ULTIMATE, hiscores[GAME_MODE.ULTIMATE]

        return GAME_MODE.IRONMAN, hiscores[GAME_MODE.IRONMAN]
