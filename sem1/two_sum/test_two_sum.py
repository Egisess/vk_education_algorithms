import pytest
from two_sum import solution_1


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 7, 13], 4, [0, 1]),
    ([1, 3, 5, 7, 13], 8, [0, 3]),
    ([1, 3, 5, 7, 13], 12, [2, 3]),
    ([1, 3, 5, 7, 13], 20, [3, 4]),
    ([1, 3, 5, 7, 13], 6, [0, 2]),
    ([1, 3, 5, 7, 13], 10, [1, 3]),
    ([1, 3, 5, 7, 13], 18, [2, 4]),
    ([1, 3, 5, 7, 13], 8, [0, 3]),
    ([1, 3, 5, 7, 13], 16, [1, 4]),
    ([1, 3, 5, 7, 13], 14, [0, 4]),
    ([1, 3], 4, [0, 1]),
    ([1, 3], 3, [-1, -1]),
    ([1], 2, [-1, -1]),
])
def test_solutions(nums, target, expected):
    assert solution_1(nums, target) == expected
