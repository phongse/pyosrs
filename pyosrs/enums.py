from enum import Enum
from typing import Dict, Final, Tuple


class GAME_MODE(Enum):
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
    24: ("league_points", "League Points"),
    25: ("bounty_hunter_hunter", "Bounty Hunter - Hunter"),
    26: ("bounty_hunter_rogue", "Bounty Hunter - Rogue"),
    27: ("bounty_hunter_hunter_legacy", "Bounty Hunter (Legacy) - Hunter"),
    28: ("bounty_hunter_rogue_legacy", "Bounty Hunter (Legacy) - Rogue"),
    36: ("lms", "LMS"),
    37: ("pvp_arena", "PvP Arena"),
    38: ("soul_wars", "Soul Wars Zeal"),
    39: ("rifts_closed", "Rifts Closed"),
}

CLUES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    29: ("all", "Clue Scrolls All"),
    30: ("beginner", "Clue Scrolls Beginner"),
    31: ("easy", "Clue Scrolls Easy"),
    32: ("medium", "Clue Scrolls Medium"),
    33: ("hard", "Clue Scrolls Hard"),
    34: ("elite", "Clue Scrolls Elite"),
    35: ("master", "Clue Scrolls Master"),
}

BOSSES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    40: ("abyssal_sire", "Abyssal Sire"),
    41: ("alchemical_hydra", "Alchemical Hydra"),
    42: ("artio", "Artio"),
    43: ("barrows_chests", "Barrows Chests"),
    44: ("bryophyta", "Bryophyta"),
    45: ("callisto", "Callisto"),
    46: ("cal_varion", "Calvarion"),
    47: ("cerberus", "Cerberus"),
    48: ("chambers_of_xeric", "Chambers of Xeric"),
    49: (
        "chambers_of_xeric_challenge_mode",
        "Chambers of Xeric: Challenge Mode",
    ),
    50: ("chaos_elemental", "Chaos Elemental"),
    51: ("chaos_fanatic", "Chaos Fanatic"),
    52: ("commander_zilyana", "Commander Zilyana"),
    53: ("corporeal_beast", "Corporeal Beast"),
    54: ("crazy_archaeologist", "Crazy Archaeologist"),
    55: ("dagannoth_prime", "Dagannoth Prime"),
    56: ("dagannoth_rex", "Dagannoth Rex"),
    57: ("dagannoth_supreme", "Dagannoth Supreme"),
    58: ("deranged_archaeologist", "Deranged Archaeologist"),
    59: ("duke_sucellus", "Duke Sucellus"),
    60: ("general_graardor", "General Graardor"),
    61: ("giant_mole", "Giant Mole"),
    62: ("grotesque_guardians", "Grotesque Guardians"),
    63: ("hespori", "Hespori"),
    64: ("kalphite_queen", "Kalphite Queen"),
    65: ("king_black_dragon", "King Black Dragon"),
    66: ("kraken", "Kraken"),
    67: ("kree_arra", "Kree'Arra"),
    68: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
    69: ("mimic", "Mimic"),
    70: ("nex", "Nex"),
    71: ("nightmare", "Nightmare"),
    72: ("phosanis_nightmare", "Phosani's Nightmare"),
    73: ("obor", "Obor"),
    74: ("phantom_muspah", "Phantom Muspah"),
    75: ("sarachnis", "Sarachnis"),
    76: ("scorpia", "Scorpia"),
    77: ("skotizo", "Skotizo"),
    78: ("spindel", "Spindel"),
    79: ("tempoross", "Tempoross"),
    80: ("the_gauntlet", "The Gauntlet"),
    81: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    82: ("the_leviathan", "The Leviathan"),
    83: ("the_whisperer", "The Whisperer"),
    84: ("theatre_of_blood", "Theatre of Blood"),
    85: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    86: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    87: ("tombs_of_amascut", "Tombs of Amascut"),
    88: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    89: ("tzkal_zuk", "TzKal-Zuk"),
    90: ("tztok_jad", "TzTok-Jad"),
    91: ("vardorvis", "Vardorvis"),
    92: ("venenatis", "Venenatis"),
    93: ("vet_ion", "Vet'ion"),
    94: ("vorkath", "Vorkath"),
    95: ("wintertodt", "Wintertodt"),
    96: ("zalcano", "Zalcano"),
    97: ("zulrah", "Zulrah"),
}

HISCORE_RESPONSE_LEN: Final[int] = (
    len(SKILLS_INDEX) + len(MINIGAMES_INDEX) + len(CLUES_INDEX) + len(BOSSES_INDEX)
)
