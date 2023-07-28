from pydantic import BaseModel

from pyosrs.enums import GAME_MODE


class Skill(BaseModel):
    rank: int = 0
    level: int = 0
    experience: int = 0


class Minigame(BaseModel):
    rank: int = 0
    score: int = 0


class Skills(BaseModel):
    overall: Skill = Skill()
    attack: Skill = Skill()
    defence: Skill = Skill()
    strength: Skill = Skill()
    hitpoints: Skill = Skill()
    ranged: Skill = Skill()
    prayer: Skill = Skill()
    magic: Skill = Skill()
    cooking: Skill = Skill()
    woodcutting: Skill = Skill()
    fletching: Skill = Skill()
    fishing: Skill = Skill()
    firemaking: Skill = Skill()
    crafting: Skill = Skill()
    smithing: Skill = Skill()
    mining: Skill = Skill()
    herblore: Skill = Skill()
    agility: Skill = Skill()
    thieving: Skill = Skill()
    slayer: Skill = Skill()
    farming: Skill = Skill()
    runecrafting: Skill = Skill()
    hunter: Skill = Skill()
    construction: Skill = Skill()


class Minigames(BaseModel):
    league_points: Minigame = Minigame()
    bounty_hunter_hunter: Minigame = Minigame()
    bounty_hunter_rogue: Minigame = Minigame()
    bounty_hunter_hunter_legacy: Minigame = Minigame()
    bounty_hunter_rogue_legacy: Minigame = Minigame()
    lms: Minigame = Minigame()
    pvp_arena: Minigame = Minigame()
    soul_wars: Minigame = Minigame()
    rifts_closed: Minigame = Minigame()


class Clues(BaseModel):
    all: Minigame = Minigame()
    beginner: Minigame = Minigame()
    easy: Minigame = Minigame()
    medium: Minigame = Minigame()
    hard: Minigame = Minigame()
    elite: Minigame = Minigame()
    master: Minigame = Minigame()


class Bosses(BaseModel):
    alchemical_hydra: Minigame = Minigame()
    artio: Minigame = Minigame()
    barrows_chests: Minigame = Minigame()
    bryophyta: Minigame = Minigame()
    callisto: Minigame = Minigame()
    cal_varion: Minigame = Minigame()
    cerberus: Minigame = Minigame()
    chambers_of_xeric: Minigame = Minigame()
    chambers_of_xeric_challenge_mode: Minigame = Minigame()
    chaos_elemental: Minigame = Minigame()
    chaos_fanatic: Minigame = Minigame()
    commander_zilyana: Minigame = Minigame()
    corporeal_beast: Minigame = Minigame()
    crazy_archaeologist: Minigame = Minigame()
    dagannoth_prime: Minigame = Minigame()
    dagannoth_rex: Minigame = Minigame()
    dagannoth_supreme: Minigame = Minigame()
    deranged_archaeologist: Minigame = Minigame()
    duke_sucellus: Minigame = Minigame()
    general_graardor: Minigame = Minigame()
    giant_mole: Minigame = Minigame()
    grotesque_guardians: Minigame = Minigame()
    hespori: Minigame = Minigame()
    kalphite_queen: Minigame = Minigame()
    king_black_dragon: Minigame = Minigame()
    kraken: Minigame = Minigame()
    kree_arra: Minigame = Minigame()
    kril_tsutsaroth: Minigame = Minigame()
    mimic: Minigame = Minigame()
    nex: Minigame = Minigame()
    nightmare: Minigame = Minigame()
    phosanis_nightmare: Minigame = Minigame()
    obor: Minigame = Minigame()
    phantom_muspah: Minigame = Minigame()
    sarachnis: Minigame = Minigame()
    scorpia: Minigame = Minigame()
    skotizo: Minigame = Minigame()
    spindel: Minigame = Minigame()
    tempoross: Minigame = Minigame()
    the_gauntlet: Minigame = Minigame()
    the_corrupted_gauntlet: Minigame = Minigame()
    the_leviathan: Minigame = Minigame()
    the_whisperer: Minigame = Minigame()
    theatre_of_blood: Minigame = Minigame()
    theatre_of_blood_hard_mode: Minigame = Minigame()
    thermonuclear_smoke_devil: Minigame = Minigame()
    tombs_of_amascut: Minigame = Minigame()
    tombs_of_amascut_expert_mode: Minigame = Minigame()
    tzkal_zuk: Minigame = Minigame()
    tztok_jad: Minigame = Minigame()
    vardorvis: Minigame = Minigame()
    venenatis: Minigame = Minigame()
    vet_ion: Minigame = Minigame()
    vorkath: Minigame = Minigame()
    wintertodt: Minigame = Minigame()
    zalcano: Minigame = Minigame()
    zulrah: Minigame = Minigame()


class Hiscore(BaseModel):
    username: str
    game_mode: GAME_MODE
    combat_level: int
    skills: Skills
    minigames: Minigames
    clues: Clues
    bosses: Bosses
