import pytest
from bin_array_sort import solution


@pytest.mark.parametrize("nums, expected", [
    ([0, 0, 0, 1, 1], [0, 0, 0, 1, 1]),
    ([1, 1, 0, 0, 0], [0, 0, 0, 1, 1]),
    ([0, 1, 0, 1, 0], [0, 0, 0, 1, 1]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([0], [0]),
    ([1], [1]),
    ([], []),
    ([1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1]),
    ([0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1]),
    ([1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1]),
])
def test_solutions(nums, expected):
    solution(nums)
    assert nums == expected