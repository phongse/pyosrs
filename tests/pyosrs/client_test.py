import asyncio
from unittest import mock

import httpx
import pytest

import testing.api_responses
from pyosrs.client import Pyosrs
from pyosrs.enums import GAME_MODE
from pyosrs.exceptions import InvalidAPIResponseException, InvalidUserException
from testing.factories import HiscoreFactory, SkillFactory, SkillsFactory
from testing.mocks import hiscore_mock


@pytest.mark.asyncio
async def test_get_hiscore():
    hiscore_mock["get_hiscore"].mock(
        side_effect=[
            httpx.Response(
                status_code=200, text=testing.api_responses.LYNX_TITAN_RESPONSE
            ),
            httpx.Response(
                status_code=200,
                text=testing.api_responses.RIP_DIDDEBOY_RESPONSE,
            ),
        ]
    )
    hiscore_mock["get_hiscore_ironman"].mock(
        side_effect=[
            httpx.Response(
                status_code=200, text=testing.api_responses.IRON_HYGER_RESPONSE
            )
        ]
    )
    async with hiscore_mock:
        async with Pyosrs() as client:
            hiscores = await asyncio.gather(
                client.get_hiscore("Lynx Titan"),
                client.get_hiscore("rip Diddeboy"),
                client.get_hiscore("Iron Hyger", GAME_MODE.IRONMAN),
            )
            lynx_titan, rip_diddeboy, iron_hyger = hiscores

        assert hiscore_mock["get_hiscore"].call_count == 2
        assert hiscore_mock["get_hiscore_ironman"].call_count == 1

    assert lynx_titan is not None
    assert lynx_titan.username == "Lynx Titan"
    assert lynx_titan.skills.overall.rank == 1
    assert lynx_titan.skills.overall.level == 2277
    assert lynx_titan.skills.overall.experience == 4600000000
    assert lynx_titan.combat_level == 126

    assert rip_diddeboy is not None
    assert rip_diddeboy.username == "rip Diddeboy"
    assert rip_diddeboy.combat_level == 1

    assert iron_hyger is not None
    assert iron_hyger.username == "Iron Hyger"
    assert iron_hyger.skills.overall.rank == 1  # Rank 1 ironman hiscore
    assert iron_hyger.skills.overall.level == 2277
    assert iron_hyger.skills.overall.experience == 4600000000
    assert iron_hyger.combat_level == 126


@pytest.mark.asyncio
async def test_clues_hiscore():
    hiscore_mock["get_hiscore"].mock(
        side_effect=[
            httpx.Response(
                status_code=200, text=testing.api_responses.LYNX_TITAN_RESPONSE
            )
        ]
    )
    async with hiscore_mock:
        async with Pyosrs() as client:
            lynx_titan = await client.get_hiscore("Lynx Titan")

    assert lynx_titan.clues.dict() == {
        "all": {"rank": 764633, "score": 22},
        "beginner": {"rank": -1, "score": -1},
        "easy": {"rank": -1, "score": -1},
        "medium": {"rank": -1, "score": -1},
        "hard": {"rank": 480613, "score": 22},
        "elite": {"rank": -1, "score": -1},
        "master": {"rank": -1, "score": -1},
    }


@pytest.mark.asyncio
async def test_get_hiscore_with_invalid_username():
    async with hiscore_mock:
        hiscore_mock["get_hiscore"].mock(side_effect=[httpx.Response(status_code=404)])
        async with Pyosrs() as client:
            with pytest.raises(InvalidUserException):
                await client.get_hiscore("invalid username")

        assert hiscore_mock["get_hiscore"].called


@pytest.mark.asyncio
async def test_get_hiscore_with_new_skill():
    async with hiscore_mock:
        hiscore_mock["get_hiscore"].mock(
            side_effect=[
                httpx.Response(
                    status_code=200, text=testing.api_responses.NEW_SKILL_RESPONSE
                )
            ]
        )
        async with Pyosrs() as client:
            with pytest.raises(InvalidAPIResponseException):
                await client.get_hiscore("invalid API response")

        assert hiscore_mock["get_hiscore"].called


@mock.patch("pyosrs.client.Pyosrs.get_hiscore")
@pytest.mark.asyncio
async def test_get_game_mode(get_hiscore_mock):
    hiscores = [
        HiscoreFactory(
            skills=SkillsFactory(overall=SkillFactory(experience=200)),
            game_mode=GAME_MODE.MAIN,
        ),
        HiscoreFactory(
            skills=SkillsFactory(overall=SkillFactory(experience=100)),
            game_mode=GAME_MODE.IRONMAN,
        ),
        HiscoreFactory(
            skills=SkillsFactory(overall=SkillFactory(experience=100)),
            game_mode=GAME_MODE.HARDCORE,
        ),
        HiscoreFactory(
            skills=SkillsFactory(overall=SkillFactory(experience=100)),
            game_mode=GAME_MODE.ULTIMATE,
        ),
    ]

    get_hiscore_mock.side_effect = hiscores
    async with Pyosrs() as client:
        game_mode, _ = await client.get_game_mode("test name")
        assert game_mode == GAME_MODE.MAIN

        hiscores[1].skills.overall.experience = 300
        get_hiscore_mock.side_effect = hiscores
        game_mode, _ = await client.get_game_mode("test name")
        assert game_mode == GAME_MODE.IRONMAN

        hiscores[2].skills.overall.experience = 400
        get_hiscore_mock.side_effect = hiscores
        game_mode, _ = await client.get_game_mode("test name")
        assert game_mode == GAME_MODE.HARDCORE

        # To test the ultimate hiscore, the hardcore hiscore cannot have a higher
        # rank than the ironman hiscore. This is because it is not possible to be
        # simultaneously ranked on both the hardcore and ultimate leaderboards.
        hiscores[2] = None
        hiscores[3].skills.overall.experience = 500
        get_hiscore_mock.side_effect = hiscores
        game_mode, _ = await client.get_game_mode("test name")
        assert game_mode == GAME_MODE.ULTIMATE


@mock.patch("pyosrs.client.Pyosrs.get_hiscore")
@pytest.mark.asyncio
async def test_get_game_mode_with_invalid_username(get_hiscore_mock):
    get_hiscore_mock.side_effect = [None for _ in range(4)]
    async with Pyosrs() as client:
        with pytest.raises(InvalidUserException):
            await client.get_game_mode("invalid username")

    ultimate = (
        HiscoreFactory(
            skills=SkillsFactory(overall=SkillFactory(experience=100)),
            game_mode=GAME_MODE.ULTIMATE,
        ),
    )
    get_hiscore_mock.side_effect = ultimate
    async with Pyosrs() as client:
        with pytest.raises(InvalidUserException):
            await client.get_game_mode("invalid username")
