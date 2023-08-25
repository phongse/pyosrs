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
    25: ("deadman_points", "Deadman Points"),
    26: ("bounty_hunter_hunter", "Bounty Hunter - Hunter"),
    27: ("bounty_hunter_rogue", "Bounty Hunter - Rogue"),
    28: ("bounty_hunter_hunter_legacy", "Bounty Hunter (Legacy) - Hunter"),
    29: ("bounty_hunter_rogue_legacy", "Bounty Hunter (Legacy) - Rogue"),
    37: ("lms", "LMS"),
    38: ("pvp_arena", "PvP Arena"),
    39: ("soul_wars", "Soul Wars Zeal"),
    40: ("rifts_closed", "Rifts Closed"),
}

CLUES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    30: ("all", "Clue Scrolls All"),
    31: ("beginner", "Clue Scrolls Beginner"),
    32: ("easy", "Clue Scrolls Easy"),
    33: ("medium", "Clue Scrolls Medium"),
    34: ("hard", "Clue Scrolls Hard"),
    35: ("elite", "Clue Scrolls Elite"),
    36: ("master", "Clue Scrolls Master"),
}

BOSSES_INDEX: Final[Dict[int, Tuple[str, str]]] = {
    41: ("abyssal_sire", "Abyssal Sire"),
    42: ("alchemical_hydra", "Alchemical Hydra"),
    43: ("artio", "Artio"),
    44: ("barrows_chests", "Barrows Chests"),
    45: ("bryophyta", "Bryophyta"),
    46: ("callisto", "Callisto"),
    47: ("cal_varion", "Calvarion"),
    48: ("cerberus", "Cerberus"),
    49: ("chambers_of_xeric", "Chambers of Xeric"),
    50: (
        "chambers_of_xeric_challenge_mode",
        "Chambers of Xeric: Challenge Mode",
    ),
    51: ("chaos_elemental", "Chaos Elemental"),
    52: ("chaos_fanatic", "Chaos Fanatic"),
    53: ("commander_zilyana", "Commander Zilyana"),
    54: ("corporeal_beast", "Corporeal Beast"),
    55: ("crazy_archaeologist", "Crazy Archaeologist"),
    56: ("dagannoth_prime", "Dagannoth Prime"),
    57: ("dagannoth_rex", "Dagannoth Rex"),
    58: ("dagannoth_supreme", "Dagannoth Supreme"),
    59: ("deranged_archaeologist", "Deranged Archaeologist"),
    60: ("duke_sucellus", "Duke Sucellus"),
    61: ("general_graardor", "General Graardor"),
    62: ("giant_mole", "Giant Mole"),
    63: ("grotesque_guardians", "Grotesque Guardians"),
    64: ("hespori", "Hespori"),
    65: ("kalphite_queen", "Kalphite Queen"),
    66: ("king_black_dragon", "King Black Dragon"),
    67: ("kraken", "Kraken"),
    68: ("kree_arra", "Kree'Arra"),
    69: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
    70: ("mimic", "Mimic"),
    71: ("nex", "Nex"),
    72: ("nightmare", "Nightmare"),
    73: ("phosanis_nightmare", "Phosani's Nightmare"),
    74: ("obor", "Obor"),
    75: ("phantom_muspah", "Phantom Muspah"),
    76: ("sarachnis", "Sarachnis"),
    77: ("scorpia", "Scorpia"),
    78: ("skotizo", "Skotizo"),
    79: ("spindel", "Spindel"),
    80: ("tempoross", "Tempoross"),
    81: ("the_gauntlet", "The Gauntlet"),
    82: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    83: ("the_leviathan", "The Leviathan"),
    84: ("the_whisperer", "The Whisperer"),
    85: ("theatre_of_blood", "Theatre of Blood"),
    86: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    87: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    88: ("tombs_of_amascut", "Tombs of Amascut"),
    89: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    90: ("tzkal_zuk", "TzKal-Zuk"),
    91: ("tztok_jad", "TzTok-Jad"),
    92: ("vardorvis", "Vardorvis"),
    93: ("venenatis", "Venenatis"),
    94: ("vet_ion", "Vet'ion"),
    95: ("vorkath", "Vorkath"),
    96: ("wintertodt", "Wintertodt"),
    97: ("zalcano", "Zalcano"),
    98: ("zulrah", "Zulrah"),
}

HISCORE_RESPONSE_LEN: Final[int] = (
    len(SKILLS_INDEX) + len(MINIGAMES_INDEX) + len(CLUES_INDEX) + len(BOSSES_INDEX)
)
