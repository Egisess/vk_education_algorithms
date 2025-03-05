import pytest
from linked_list_merge import linked_list_merge
from sem2.linked_list import *


@pytest.mark.parametrize("A, B, expected", [
    (LinkedList([1, 3, 5]), LinkedList([2, 4, 6]), LinkedList([1, 2, 3, 4, 5, 6])),
    (LinkedList([1, 2, 3]), LinkedList([4, 5, 6]), LinkedList([1, 2, 3, 4, 5, 6])),
    (LinkedList([]), LinkedList([1, 2, 3]), LinkedList([1, 2, 3])),
    (LinkedList([1, 2, 3]), LinkedList([]), LinkedList([1, 2, 3])),
    (LinkedList([]), LinkedList([]), LinkedList([])),
    (LinkedList([1, 1, 1]), LinkedList([1, 1, 1]), LinkedList([1, 1, 1, 1, 1, 1])),
    (LinkedList([1, 3, 5]), LinkedList([2, 3, 6]), LinkedList([1, 2, 3, 3, 5, 6])),
    (LinkedList([1, 4, 5]), LinkedList([2, 3, 6]), LinkedList([1, 2, 3, 4, 5, 6]))
])
def test_linked_list_merge(A, B, expected):
    assert linked_list_merge(A, B) == expected
