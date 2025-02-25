import pytest
from partially_inverse_array import solution


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3], 0, [1, 2, 3]),
    ([1, 2, 3], 1, [3, 1, 2]),
    ([1, 2, 3], 2, [2, 3, 1]),
    ([1, 2, 3], 3, [1, 2, 3]),
    ([1, 2, 3], 6, [1, 2, 3]),
    ([1, 2, 3], -3, [1, 2, 3]),
    ([1, 2, 3], -2, [3, 1, 2]),
    ([1, 2, 3], -1, [2, 3, 1]),
    ([1], 1, [1]),
    ([1], 256, [1]),
    ([], 0, []),
])
def test_solutions(nums, k, expected):
    assert solution(nums, k) == expected
