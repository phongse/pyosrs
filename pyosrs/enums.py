from enum import Enum
from types import MappingProxyType
from typing import Final, Tuple


class GAME_MODE(Enum):
    MAIN: str = "hiscore_oldschool"
    IRONMAN: str = "hiscore_oldschool_ironman"
    HARDCORE: str = "hiscore_oldschool_hardcore_ironman"
    ULTIMATE: str = "hiscore_oldschool_ultimate"
    DEADMAN: str = "hiscore_oldschool_deadman"
    SEASONAL: str = "hiscore_oldschool_seasonal"
    TOURNAMENT: str = "hiscore_oldschool_tournament"
    FRESH_START: str = "hiscore_oldschool_fresh_start"


SKILLS_INDEX: Final[MappingProxyType[int, Tuple[str, str]]] = MappingProxyType(
    {
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
)

MINIGAMES_INDEX: Final[MappingProxyType[int, Tuple[str, str]]] = MappingProxyType(
    {
        24: ("league_points", "League Points"),
        25: ("bounty_hunter_hunter", "Bounty Hunter - Hunter"),
        26: ("bounty_hunter_rogue", "Bounty Hunter - Rogue"),
        34: ("lms", "LMS"),
        35: ("pvp_arena", "PvP Arena"),
        36: ("soul_wars", "Soul Wars Zeal"),
        37: ("rifts_closed", "Rifts Closed"),
    }
)

CLUES_INDEX: Final[MappingProxyType[int, Tuple[str, str]]] = MappingProxyType(
    {
        27: ("all", "All"),
        28: ("beginner", "Beginner"),
        29: ("easy", "Easy"),
        30: ("medium", "Medium"),
        31: ("hard", "Hard"),
        32: ("elite", "Elite"),
        33: ("master", "Master"),
    }
)

BOSSES_INDEX: Final[MappingProxyType[int, Tuple[str, str]]] = MappingProxyType(
    {
        38: ("abyssal_sire", "Abyssal Sire"),
        39: ("alchemical_hydra", "Alchemical Hydra"),
        40: ("artio", "Artio"),
        41: ("barrows_chests", "Barrows Chests"),
        42: ("bryophyta", "Bryophyta"),
        43: ("callisto", "Callisto"),
        44: ("cal_varion", "Calvarion"),
        45: ("cerberus", "Cerberus"),
        46: ("chambers_of_xeric", "Chambers of Xeric"),
        47: (
            "chambers_of_xeric_challenge_mode",
            "Chambers of Xeric: Challenge Mode",
        ),
        48: ("chaos_elemental", "Chaos Elemental"),
        49: ("chaos_fanatic", "Chaos Fanatic"),
        50: ("commander_zilyana", "Commander Zilyana"),
        51: ("corporeal_beast", "Corporeal Beast"),
        52: ("crazy_archaeologist", "Crazy Archaeologist"),
        53: ("dagannoth_prime", "Dagannoth Prime"),
        54: ("dagannoth_rex", "Dagannoth Rex"),
        55: ("dagannoth_supreme", "Dagannoth Supreme"),
        56: ("deranged_archaeologist", "Deranged Archaeologist"),
        57: ("general_graardor", "General Graardor"),
        58: ("giant_mole", "Giant Mole"),
        59: ("grotesque_guardians", "Grotesque Guardians"),
        60: ("hespori", "Hespori"),
        61: ("kalphite_queen", "Kalphite Queen"),
        62: ("king_black_dragon", "King Black Dragon"),
        63: ("kraken", "Kraken"),
        64: ("kree_arra", "Kree'Arra"),
        65: ("kril_tsutsaroth", "K'ril Tsutsaroth"),
        66: ("mimic", "Mimic"),
        67: ("nex", "Nex"),
        68: ("nightmare", "Nightmare"),
        69: ("phosanis_nightmare", "Phosani's Nightmare"),
        70: ("obor", "Obor"),
        71: ("phantom_muspah", "Phantom Muspah"),
        72: ("sarachnis", "Sarachnis"),
        73: ("scorpia", "Scorpia"),
        74: ("skotizo", "Skotizo"),
        75: ("spindel", "Spindel"),
        76: ("tempoross", "Tempoross"),
        77: ("the_gauntlet", "The Gauntlet"),
        78: ("the_corrupted_gauntlet", "The Corrupted Gauntlet"),
        79: ("theatre_of_blood", "Theatre of Blood"),
        80: ("theatre_of_blood_hard_mode", "Theatre of Blood: Hard Mode"),
        81: ("thermonuclear_smoke_devil", "Thermonuclear Smoke Devil"),
        82: ("tombs_of_amascut", "Tombs of Amascut"),
        83: ("tombs_of_amascut_expert_mode", "Tombs of Amascut: Expert Mode"),
        84: ("tzkal_zuk", "TzKal-Zuk"),
        85: ("tztok_jad", "TzTok-Jad"),
        86: ("venenatis", "Venenatis"),
        87: ("vet_ion", "Vet'ion"),
        88: ("vorkath", "Vorkath"),
        89: ("wintertodt", "Wintertodt"),
        90: ("zalcano", "Zalcano"),
        91: ("zulrah", "Zulrah"),
    }
)

HISCORE_RESPONSE_LEN: Final[int] = (
    len(SKILLS_INDEX) + len(MINIGAMES_INDEX) + len(CLUES_INDEX) + len(BOSSES_INDEX)
)
