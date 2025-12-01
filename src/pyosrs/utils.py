def base(defence: int, hitpoints: int, prayer: int) -> float:
    return (1 / 4) * (defence + hitpoints + int(prayer * 0.5))


def melee(attack: int, strength: int) -> float:
    return (13 / 40) * (attack + strength)


def range(ranged: int) -> float:
    return (13 / 40) * int(ranged * (3 / 2))


def mage(magic: int) -> float:
    return (13 / 40) * int(magic * (3 / 2))


def calc_combat_level(
    defence: int,
    hitpoints: int,
    prayer: int,
    attack: int,
    strength: int,
    ranged: int,
    magic: int,
) -> int:
    if any(
        arg < 1 for arg in (defence, hitpoints, prayer, attack, strength, ranged, magic)
    ):
        raise ValueError("All arguments must be greater than 0.")
    baselevel = base(defence, hitpoints, prayer)
    max_combat = max(
        melee(attack, strength),
        range(ranged),
        mage(magic),
    )
    return int(baselevel + max_combat)
