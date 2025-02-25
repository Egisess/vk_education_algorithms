import pytest
from even_first import even_first

@pytest.mark.parametrize("nums, expected_evens, expected_odds_set", [
    ([3, 2, 4, 1, 11, 8, 9], [2, 4, 8], {3, 1, 11, 9}),
    ([2, 4, 6, 8], [2, 4, 6, 8], set()),
    ([1, 3, 5, 7], [], {1, 3, 5, 7}),
    ([2, 4, 1, 3], [2, 4], {1, 3}),
    ([], [], set()),
    ([2], [2], set()),
    ([1], [], {1}),
    ([3, 2, 4, 1, 11, 8, 9, 10, 12, 15], [2, 4, 8, 10, 12], {3, 1, 11, 9, 15}),
    ([1, 3, 5, 2, 4], [2, 4], {1, 3, 5}),
    ([1, 3, 2, 4, 5], [2, 4], {1, 3, 5}),
    ([1, 2, 3, 4, 5, 6], [2, 4, 6], {1, 3, 5}),
])
def test_merge_sorted_arrays(nums, expected_evens, expected_odds_set):
    even_first(nums)
    assert nums[:len(expected_evens)] == expected_evens
    assert set(nums[len(expected_evens):]) == expected_odds_set
