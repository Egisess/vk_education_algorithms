import pytest
from cycled_list import cycled_list
from sem2.linked_list import *


@pytest.mark.parametrize("head, has_cycle", [
    (LinkedList([]).dummy_head, False),
    (LinkedList([1]).dummy_head, False),
    (LinkedList([1]).make_cycle([[0, 0]]).dummy_head, True),
    (LinkedList([1, 2, 3, 4]).dummy_head, False),
    (LinkedList([1, 2, 3, 4]).make_cycle([[0, 3]]).dummy_head, True),
])
def test_cycled_linked_list(head, has_cycle):
    assert cycled_list(head) == has_cycle
