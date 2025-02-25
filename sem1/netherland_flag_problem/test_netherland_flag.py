import pytest
from netherland_flag import netherland_flag

@pytest.mark.parametrize("nums, expected", [
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ([0, 0, 0], [0, 0, 0]),
    ([1, 1, 1], [1, 1, 1]),
    ([2, 2, 2], [2, 2, 2]),
    ([0, 0, 1, 1, 2, 2], [0, 0, 1, 1, 2, 2]),
    ([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]),
    ([], []),
    ([0], [0]),
    ([1], [1]),
    ([2], [2]),
    ([0, 1, 0, 1], [0, 0, 1, 1]),
    ([1, 2, 2, 1], [1, 1, 2, 2]),
    ([0, 2, 0, 2], [0, 0, 2, 2]),
    ([2, 0, 1, 2, 1, 0, 2, 0, 1], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
])
def test_netherland_flag(nums, expected):
    netherland_flag(nums)
    assert nums == expected