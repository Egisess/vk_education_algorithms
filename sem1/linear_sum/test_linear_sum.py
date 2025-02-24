import pytest
from linear_sum import solution_1, solution_2


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (5, 15),
    (10, 55),
    (100, 5050),
])
def test_solutions(n, expected):
    assert solution_1(n) == expected
    assert solution_2(n) == expected
