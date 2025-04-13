import pytest
from twoSum import twoSum

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [2, 7]),
    ([3, 2, 4], 6, [2, 4]),
    ([3, 3], 6, [3, 3]),
    ([-1, -2, -3, -4, -5], -8, [-3, -5]),
    ([0, 1, 2, 3], 3, [0, 3]),
     ([0, 1, 2, 3], 6, []),
    ([1000, 2000, 3000], 4000, [1000, 3000]),
    ([4, 1, 4, 9, 7], 8, [4, 4]),
    ([1, 2, 3, 4, 5], 9, [4, 5]),
    ([5, 1, 3, 4, 2], 6, [5, 1]),
    ([5, 5, 5, 5], 10, [5, 5]),
    ([1, 2], 3, [1, 2]),
    ([-3, 4, 3, 90], 0, [-3, 3]),
])
def test_twoSum(nums, target, expected):
    result = twoSum(nums, target)
    assert sorted(result) == sorted(expected)