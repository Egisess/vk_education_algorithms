import pytest
from shellSort import shellSort

@pytest.mark.parametrize("a", [
    ([-1, 2, -3, 10, 0, -4]),
    ([-1, -1, -1, -1]),
    ([0, 10, -1, 2, 25]),
])
def test_stringDifference(a):
    assert shellSort(a) == sorted(a)