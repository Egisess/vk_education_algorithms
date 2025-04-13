import pytest
from binarySearchSqrt import binarySearchSqrt

@pytest.mark.parametrize("num, expected", [
    (0, 0),
    (1, 1),
    (4, 2),
    (9, 3),
    (10, 3),
    (15, 4),
    (16, 4)
])
def test_binarySearchSqrt(num, expected):
    assert binarySearchSqrt(num) == expected
