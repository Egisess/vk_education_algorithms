import pytest
from quadroberFeed import quadroberFeed

@pytest.mark.parametrize("animals, food, expected", [
    ([1, 2, 3, 4], [0 ,0], 0),
    ([1, 2, 3, 4], [1, 1], 1),
    ([1, 2, 3, 4], [1, 4], 2),
    ([4, 4, 4, 4], [5, 6, 7], 3),
])
def test_quadroberFeed(animals, food, expected):
    assert quadroberFeed(animals, food) == expected
