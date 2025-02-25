import pytest
from two_sum import solution_1

test_nums = [1, 3, 5, 7, 13]


@pytest.mark.parametrize("nums, target, expected", [
    (test_nums, 4, [[0, 1]]),
    (test_nums, 8, [[0, 3], [1, 2]]),
    (test_nums, 12, [[2, 3]]),
    (test_nums, 20, [[3, 4]]),
    (test_nums, 6, [[0, 2]]),
    (test_nums, 10, [[1, 3]]),
    (test_nums, 18, [[2, 4]]),
    (test_nums, 8, [[0, 3], [1, 2]]),
    (test_nums, 16, [[1, 4]]),
    (test_nums, 14, [[0, 4]]),
    ([-1, 1], 0, [[0, 1]]),
    ([1, 3], 4, [[0, 1]]),
    ([1, 3], 3, [[]]),
    ([1], 2, [[]]),
])
def test_solutions(nums, target, expected):
    assert solution_1(nums, target) in expected
