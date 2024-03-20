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
    17: ("colosseum_glory", "Colosseum Glory"),
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
    18: ("abyssal_sire", "Abyssal Sire"),
    19: ("alchemical_hydra", "Alchemical Hydra"),
    20: ("artio", "Artio"),
    21: ("barrows_chests", "Barrows Chests"),
    22: ("bryophyta", "Bryophyta"),
    23: ("callisto", "Callisto"),
    24: ("cal_varion", "Calvarion"),
    25: ("cerberus", "Cerberus"),
    26: ("chambers_of_xeric", "Chambers of Xeric"),
    27: (
        "chambers_of_xeric_challenge_mode",
        "Chambers of Xeric: Challenge Mode",
    ),
    28: ("chaos_elemental", "Chaos Elemental"),
    29: ("chaos_fanatic", "Chaos Fanatic"),
    30: ("commander_zilyana", "Commander Zilyana"),
    31: ("corporeal_beast", "Corporeal Beast"),
    32: ("crazy_archaeologist", "Crazy Archaeologist"),
    33: ("dagannoth_prime", "Dagannoth Prime"),
    34: ("dagannoth_rex", "Dagannoth Rex"),
    35: ("dagannoth_supreme", "Dagannoth Supreme"),
    36: ("deranged_archaeologist", "Deranged Archaeologist"),
    37: ("duke_sucellus", "Duke Sucellus"),
    38: ("general_graardor", "General Graardor"),
    39: ("giant_mole", "Giant Mole"),
    40: ("grotesque_guardians", "Grotesque Guardians"),
    41: ("hespori", "Hespori"),
    42: ("kalphite_queen", "Kalphite Queen"),
    43: ("king_black_dragon", "King Black Dragon"),
    44: ("kraken", "Kraken"),
    45: ("kree_arra", "Kree'Arra"),
    46: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
    47: ("lunar_chests", "Lunar Chests"),
    48: ("mimic", "Mimic"),
    49: ("nex", "Nex"),
    50: ("nightmare", "Nightmare"),
    51: ("phosanis_nightmare", "Phosani's Nightmare"),
    52: ("obor", "Obor"),
    53: ("phantom_muspah", "Phantom Muspah"),
    54: ("sarachnis", "Sarachnis"),
    55: ("scorpia", "Scorpia"),
    56: ("scurrius", "Scurrius"),
    57: ("skotizo", "Skotizo"),
    58: ("sol_heredit", "Sol Heredit"),
    59: ("spindel", "Spindel"),
    60: ("tempoross", "Tempoross"),
    61: ("the_gauntlet", "The Gauntlet"),
    62: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
    63: ("the_leviathan", "The Leviathan"),
    64: ("the_whisperer", "The Whisperer"),
    65: ("theatre_of_blood", "Theatre of Blood"),
    66: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
    67: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
    68: ("tombs_of_amascut", "Tombs of Amascut"),
    69: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
    70: ("tzkal_zuk", "TzKal-Zuk"),
    71: ("tztok_jad", "TzTok-Jad"),
    72: ("vardorvis", "Vardorvis"),
    73: ("venenatis", "Venenatis"),
    74: ("vet_ion", "Vet'ion"),
    75: ("vorkath", "Vorkath"),
    76: ("wintertodt", "Wintertodt"),
    77: ("zalcano", "Zalcano"),
    78: ("zulrah", "Zulrah"),
}
