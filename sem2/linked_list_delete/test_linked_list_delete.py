import pytest
from linked_list_delete import linked_list_delete
from sem2.linked_list import *


@pytest.mark.parametrize("head, val,expected", [
    (LinkedList([1, 2, 3, 4, 5]), 1, LinkedList([2, 3, 4, 5])),
    (LinkedList([1, 2, 3, 4]), 3, LinkedList([1, 2, 4])),
    (LinkedList([1]), 1, LinkedList()),
    (LinkedList([1, 2]), 2, LinkedList([1])),
    (LinkedList(), -999, LinkedList()),
])
def test_cycled_linked_list(head, val, expected):
    assert linked_list_delete(head, val) == expected
