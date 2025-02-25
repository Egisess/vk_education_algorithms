import pytest
from merge_2_sorted_arrays import merge_sorted_arrays


@pytest.mark.parametrize("arr1, arr2, expected", [
    ([], [], []),
    ([], [1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [], [1, 2, 3]),
    ([1], [2], [1, 2]),
    ([2], [1], [1, 2]),
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 4], [3, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 2, 3], [2, 3, 4, 4], [1, 2, 2, 2, 3, 3, 4, 4]),
    ([1, 2, 3], [2], [1, 2, 2, 3]),
    ([2], [1, 2, 3], [1, 2, 2, 3]),
    ([-3, -1, 0], [-2, 1, 2], [-3, -2, -1, 0, 1, 2]),
    ([-5, 0, 5], [-4, 4], [-5, -4, 0, 4, 5]),
])
def test_merge_sorted_arrays(arr1, arr2, expected):
    assert merge_sorted_arrays(arr1, arr2) == expected
