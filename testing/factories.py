import factory

from pyosrs.enums import GAME_MODE
from pyosrs.models import Bosses, Clues, Hiscore, Minigame, Minigames, Skill, Skills


class SkillFactory(factory.Factory):
    class Meta:
        model = Skill

    rank = factory.Faker("pyint", min_value=1, max_value=99999)
    level = factory.Faker("pyint", min_value=1, max_value=99)
    experience = factory.Faker("pyint", min_value=0, max_value=200000000)


class SkillsFactory(factory.Factory):
    class Meta:
        model = Skills

    overall = SkillFactory()
    attack = SkillFactory()
    defence = SkillFactory()
    strength = SkillFactory()
    hitpoints = SkillFactory()
    ranged = SkillFactory()
    prayer = SkillFactory()
    magic = SkillFactory()
    cooking = SkillFactory()
    woodcutting = SkillFactory()
    fletching = SkillFactory()
    fishing = SkillFactory()
    firemaking = SkillFactory()
    crafting = SkillFactory()
    smithing = SkillFactory()
    mining = SkillFactory()
    herblore = SkillFactory()
    agility = SkillFactory()
    thieving = SkillFactory()
    slayer = SkillFactory()
    farming = SkillFactory()
    runecraft = SkillFactory()
    hunter = SkillFactory()
    construction = SkillFactory()


class MinigameFactory(factory.Factory):
    class Meta:
        model = Minigame

    rank = factory.Faker("pyint", min_value=1, max_value=99999)
    score = factory.Faker("pyint", min_value=0, max_value=200000000)


class MinigamesFactory(factory.Factory):
    class Meta:
        model = Minigames

    league_points = MinigameFactory()
    bounty_hunter_hunter = MinigameFactory()
    bounty_hunter_rogue = MinigameFactory()
    lms = MinigameFactory()
    pvp_arena = MinigameFactory()
    soul_wars = MinigameFactory()
    rifts_closed = MinigameFactory()


class CluesFactory(factory.Factory):
    class Meta:
        model = Clues

    all = MinigameFactory()
    beginner = MinigameFactory()
    easy = MinigameFactory()
    medium = MinigameFactory()
    hard = MinigameFactory()
    elite = MinigameFactory()
    master = MinigameFactory()


class BossesFactory(factory.Factory):
    class Meta:
        model = Bosses

    alchemical_hydra = MinigameFactory()
    artio = MinigameFactory()
    barrows_chests = MinigameFactory()
    bryophyta = MinigameFactory()
    callisto = MinigameFactory()
    cal_varion = MinigameFactory()
    cerberus = MinigameFactory()
    chambers_of_xeric = MinigameFactory()
    chambers_of_xeric_challenge_mode = MinigameFactory()
    chaos_elemental = MinigameFactory()
    chaos_fanatic = MinigameFactory()
    commander_zilyana = MinigameFactory()
    corporeal_beast = MinigameFactory()
    crazy_archaeologist = MinigameFactory()
    dagannoth_prime = MinigameFactory()
    dagannoth_rex = MinigameFactory()
    dagannoth_supreme = MinigameFactory()
    deranged_archaeologist = MinigameFactory()
    general_graardor = MinigameFactory()
    giant_mole = MinigameFactory()
    grotesque_guardians = MinigameFactory()
    hespori = MinigameFactory()
    kalphite_queen = MinigameFactory()
    king_black_dragon = MinigameFactory()
    kraken = MinigameFactory()
    kree_arra = MinigameFactory()
    kril_tsutsaroth = MinigameFactory()
    mimic = MinigameFactory()
    nex = MinigameFactory()
    nightmare = MinigameFactory()
    phosanis_nightmare = MinigameFactory()
    obor = MinigameFactory()
    phantom_muspah = MinigameFactory()
    sarachnis = MinigameFactory()
    scorpia = MinigameFactory()
    skotizo = MinigameFactory()
    spindel = MinigameFactory()
    tempoross = MinigameFactory()
    the_gauntlet = MinigameFactory()
    the_corrupted_gauntlet = MinigameFactory()
    theatre_of_blood = MinigameFactory()
    theatre_of_blood_hard_mode = MinigameFactory()
    thermonuclear_smoke_devil = MinigameFactory()
    tombs_of_amascut = MinigameFactory()
    tombs_of_amascut_expert_mode = MinigameFactory()
    tzkal_zuk = MinigameFactory()
    tztok_jad = MinigameFactory()
    venenatis = MinigameFactory()
    vet_ion = MinigameFactory()
    vorkath = MinigameFactory()
    wintertodt = MinigameFactory()
    zalcano = MinigameFactory()
    zulrah = MinigameFactory()


class HiscoreFactory(factory.Factory):
    class Meta:
        model = Hiscore

    username = factory.Faker("user_name")
    game_mode = GAME_MODE.MAIN
    combat_level = factory.Faker("pyint", min_value=1, max_value=126)
    skills = SkillsFactory()
    minigames = MinigamesFactory()
    clues = CluesFactory()
    bosses = BossesFactory()
