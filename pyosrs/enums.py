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
    78: ("scurrius", "Scurrius"),
    79: ("skotizo", "Skotizo"),
    80: ("spindel", "Spindel"),
    81: ("tempoross", "Tempoross"),
    82: ("the_gauntlet", "The Gauntlet"),
    83: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    84: ("the_leviathan", "The Leviathan"),
    85: ("the_whisperer", "The Whisperer"),
    86: ("theatre_of_blood", "Theatre of Blood"),
    87: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    88: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    89: ("tombs_of_amascut", "Tombs of Amascut"),
    90: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    91: ("tzkal_zuk", "TzKal-Zuk"),
    92: ("tztok_jad", "TzTok-Jad"),
    93: ("vardorvis", "Vardorvis"),
    94: ("venenatis", "Venenatis"),
    95: ("vet_ion", "Vet'ion"),
    96: ("vorkath", "Vorkath"),
    97: ("wintertodt", "Wintertodt"),
    98: ("zalcano", "Zalcano"),
    99: ("zulrah", "Zulrah"),
}
