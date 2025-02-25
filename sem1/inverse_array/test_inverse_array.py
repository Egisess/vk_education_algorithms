import pytest
from inverse_array import solution_1, solution_2


@pytest.mark.parametrize("nums, expected", [
    ([-2, -1, 0, 1, 2], [2, 1, 0, -1, -2]),
    ([2, 1, 0, -1, -2], [-2, -1, 0, 1, 2]),
    ([1, 1, 2], [2, 1, 1]),
    ([1], [1]),
    ([], []),
])
def test_solutions(nums, expected):
    assert solution_1(nums) == expected
    assert solution_2(nums) == expected
