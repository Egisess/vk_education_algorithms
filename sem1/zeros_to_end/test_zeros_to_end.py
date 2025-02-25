import pytest
from zeros_to_end import zeros_to_end


@pytest.mark.parametrize("nums, expected", [
    ([0, 0, 1, 0, 3, 12], [1, 3, 12, 0, 0, 0]),
    ([0, 33, 57, 88, 60, 0, 0, 80, 99], [33, 57, 88, 60, 80, 99, 0, 0, 0]),
    ([0, 0, 0, 18, 16, 0, 0, 77, 99], [18, 16, 77, 99, 0, 0, 0, 0, 0]),
    ([0, 1, 0, 2, 0, 3, 0, 4, 0, 5], [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]),
    ([0, 4, 4, 5, 0, 0, 0, 1, 1, 2], [4, 4, 5, 1, 1, 2, 0, 0, 0, 0]),
    ([0], [0]),
    ([1], [1]),
    ([], [])
])
def test_merge_sorted_arrays(nums, expected):
    zeros_to_end(nums)
    assert nums == expected
