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
    29: ("clue_scrolls_all", "Clue Scrolls All"),
    30: ("clue_scrolls_beginner", "Clue Scrolls Beginner"),
    31: ("clue_scrolls_easy", "Clue Scrolls Easy"),
    32: ("clue_scrolls_medium", "Clue Scrolls Medium"),
    33: ("clue_scrolls_hard", "Clue Scrolls Hard"),
    34: ("clue_scrolls_elite", "Clue Scrolls Elite"),
    35: ("clue_scrolls_master", "Clue Scrolls Master"),
    36: ("lms", "LMS"),
    37: ("pvp_arena", "PvP Arena"),
    38: ("soul_wars", "Soul Wars Zeal"),
    39: ("rifts_closed", "Rifts Closed"),
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
    59: ("general_graardor", "General Graardor"),
    60: ("giant_mole", "Giant Mole"),
    61: ("grotesque_guardians", "Grotesque Guardians"),
    62: ("hespori", "Hespori"),
    63: ("kalphite_queen", "Kalphite Queen"),
    64: ("king_black_dragon", "King Black Dragon"),
    65: ("kraken", "Kraken"),
    66: ("kree_arra", "Kree'Arra"),
    67: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
    68: ("mimic", "Mimic"),
    69: ("nex", "Nex"),
    70: ("nightmare", "Nightmare"),
    71: ("phosanis_nightmare", "Phosani's Nightmare"),
    72: ("obor", "Obor"),
    73: ("phantom_muspah", "Phantom Muspah"),
    74: ("sarachnis", "Sarachnis"),
    75: ("scorpia", "Scorpia"),
    76: ("skotizo", "Skotizo"),
    77: ("spindel", "Spindel"),
    78: ("tempoross", "Tempoross"),
    79: ("the_gauntlet", "The Gauntlet"),
    80: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    81: ("theatre_of_blood", "Theatre of Blood"),
    82: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    83: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    84: ("tombs_of_amascut", "Tombs of Amascut"),
    85: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    86: ("tzkal_zuk", "TzKal-Zuk"),
    87: ("tztok_jad", "TzTok-Jad"),
    88: ("venenatis", "Venenatis"),
    89: ("vet_ion", "Vet'ion"),
    90: ("vorkath", "Vorkath"),
    91: ("wintertodt", "Wintertodt"),
    92: ("zalcano", "Zalcano"),
    93: ("zulrah", "Zulrah"),
}

HISCORE_RESPONSE_LEN: Final[int] = (
    len(SKILLS_INDEX) + len(MINIGAMES_INDEX) + len(BOSSES_INDEX)
)
