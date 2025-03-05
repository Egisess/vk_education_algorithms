import pytest
from is_original import is_original, is_original_2


@pytest.mark.parametrize("A, B, expected", [
    ([0], [0, 1, 2, 3], True),
    ([0, 1], [1, 2, 3, 0, 2, 0], False),
    ([], [1, 2, 3], True),
    ([], [], True),
    ([1, 2, 3], [], False)

])
def test_cycled_linked_list(A, B, expected):
    assert is_original(A, B) == expected
    assert is_original_2(A, B) == expected
