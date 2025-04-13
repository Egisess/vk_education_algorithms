import pytest
from annagramsGropping import annagramsGroupping

@pytest.mark.parametrize("arr, expected", [
    (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
    (["won","now","aaa","ooo","ooo"], [["won","now"],["aaa"],["ooo","ooo"]]),
])
def test_binarySearchSqrt(arr, expected):
    assert annagramsGroupping(arr) == expected
