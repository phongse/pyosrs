from enum import Enum
from typing import Dict, Final, Tuple


class GAME_MODE(Enum):  # noqa
    MAIN: str = "hiscore_oldschool"
    IRONMAN: str = "hiscore_oldschool_ironman"
    HARDCORE: str = "hiscore_oldschool_hardcore_ironman"
    ULTIMATE: str = "hiscore_oldschool_ultimate"
    DEADMAN: str = "hiscore_oldschool_deadman"
    SEASONAL: str = "hiscore_oldschool_seasonal"
    TOURNAMENT: str = "hiscore_oldschool_tournament"
    FRESH_START: str = "hiscore_oldschool_fresh_start"


SKILLS_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    0: ("overall", "Overall"),
    1: ("attack", "Attack"),
    2: ("defence", "Defence"),
    3: ("strength", "Strength"),
    4: ("hitpoints", "Hitpoints"),
    5: ("ranged", "Ranged"),
    6: ("prayer", "Prayer"),
    7: ("magic", "Magic"),
    8: ("cooking", "Cooking"),
    9: ("woodcutting", "Woodcutting"),
    10: ("fletching", "Fletching"),
    11: ("fishing", "Fishing"),
    12: ("firemaking", "Firemaking"),
    13: ("crafting", "Crafting"),
    14: ("smithing", "Smithing"),
    15: ("mining", "Mining"),
    16: ("herblore", "Herblore"),
    17: ("agility", "Agility"),
    18: ("thieving", "Thieving"),
    19: ("slayer", "Slayer"),
    20: ("farming", "Farming"),
    21: ("runecrafting", "Runecrafting"),
    22: ("hunter", "Hunter"),
    23: ("construction", "Construction"),
}

MINIGAMES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    0: ("league_points", "League Points"),
    1: ("deadman_points", "Deadman Points"),
    2: ("bounty_hunter_hunter", "Bounty Hunter - Hunter"),
    3: ("bounty_hunter_rogue", "Bounty Hunter - Rogue"),
    4: ("bounty_hunter_hunter_legacy", "Bounty Hunter (Legacy) - Hunter"),
    5: ("bounty_hunter_rogue_legacy", "Bounty Hunter (Legacy) - Rogue"),
    13: ("lms", "LMS"),
    14: ("pvp_arena", "PvP Arena"),
    15: ("soul_wars", "Soul Wars Zeal"),
    16: ("rifts_closed", "Rifts Closed"),
}

CLUES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    6: ("all", "Clue Scrolls (all)"),
    7: ("beginner", "Clue Scrolls (beginner)"),
    8: ("easy", "Clue Scrolls (easy)"),
    9: ("medium", "Clue Scrolls (medium)"),
    10: ("hard", "Clue Scrolls (hard)"),
    11: ("elite", "Clue Scrolls (elite)"),
    12: ("master", "Clue Scrolls (master)"),
}

BOSSES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    17: ("abyssal_sire", "Abyssal Sire"),
    18: ("alchemical_hydra", "Alchemical Hydra"),
    19: ("artio", "Artio"),
    20: ("barrows_chests", "Barrows Chests"),
    21: ("bryophyta", "Bryophyta"),
    22: ("callisto", "Callisto"),
    23: ("cal_varion", "Calvarion"),
    24: ("cerberus", "Cerberus"),
    25: ("chambers_of_xeric", "Chambers of Xeric"),
    26: (
        "chambers_of_xeric_challenge_mode",
        "Chambers of Xeric: Challenge Mode",
    ),
    27: ("chaos_elemental", "Chaos Elemental"),
    28: ("chaos_fanatic", "Chaos Fanatic"),
    29: ("commander_zilyana", "Commander Zilyana"),
    30: ("corporeal_beast", "Corporeal Beast"),
    31: ("crazy_archaeologist", "Crazy Archaeologist"),
    32: ("dagannoth_prime", "Dagannoth Prime"),
    33: ("dagannoth_rex", "Dagannoth Rex"),
    34: ("dagannoth_supreme", "Dagannoth Supreme"),
    35: ("deranged_archaeologist", "Deranged Archaeologist"),
    36: ("duke_sucellus", "Duke Sucellus"),
    37: ("general_graardor", "General Graardor"),
    38: ("giant_mole", "Giant Mole"),
    39: ("grotesque_guardians", "Grotesque Guardians"),
    40: ("hespori", "Hespori"),
    41: ("kalphite_queen", "Kalphite Queen"),
    42: ("king_black_dragon", "King Black Dragon"),
    43: ("kraken", "Kraken"),
    44: ("kree_arra", "Kree'Arra"),
    45: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
    46: ("mimic", "Mimic"),
    47: ("nex", "Nex"),
    48: ("nightmare", "Nightmare"),
    49: ("phosanis_nightmare", "Phosani's Nightmare"),
    50: ("obor", "Obor"),
    51: ("phantom_muspah", "Phantom Muspah"),
    52: ("sarachnis", "Sarachnis"),
    53: ("scorpia", "Scorpia"),
    54: ("scurrius", "Scurrius"),
    55: ("skotizo", "Skotizo"),
    56: ("spindel", "Spindel"),
    57: ("tempoross", "Tempoross"),
    58: ("the_gauntlet", "The Gauntlet"),
    59: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    60: ("the_leviathan", "The Leviathan"),
    61: ("the_whisperer", "The Whisperer"),
    62: ("theatre_of_blood", "Theatre of Blood"),
    63: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    64: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    65: ("tombs_of_amascut", "Tombs of Amascut"),
    66: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    67: ("tzkal_zuk", "TzKal-Zuk"),
    68: ("tztok_jad", "TzTok-Jad"),
    69: ("vardorvis", "Vardorvis"),
    70: ("venenatis", "Venenatis"),
    71: ("vet_ion", "Vet'ion"),
    72: ("vorkath", "Vorkath"),
    73: ("wintertodt", "Wintertodt"),
    74: ("zalcano", "Zalcano"),
    75: ("zulrah", "Zulrah"),
}
