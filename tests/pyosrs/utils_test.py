import pytest

from pyosrs.utils import calc_combat_level
from testing.factories import HiscoreFactory


@pytest.mark.parametrize(
    "input, expected",
    [
        # defence, hitpoints, prayer, attack, strength, ranged, magic
        ([10, 10, 10, 10, 10, 10, 10], 12),
        ([20, 20, 20, 20, 20, 20, 20], 25),
        ([44, 43, 56, 99, 1, 23, 77], 66),
        ([99, 99, 99, 99, 99, 99, 99], 126),
        ([1, 1, 1, 1, 1, 1, 1], 1),
        ([-99, -99, -99, -99, -99, -99, -99], ValueError),
    ],
)
def test_calc_combat_level(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calc_combat_level(*input)
    else:
        assert calc_combat_level(*input) == expected
