import pytest
from reverse_list import reverse_linked_list
from sem2.linked_list import *


@pytest.mark.parametrize("head, expected", [
    (LinkedList([]), LinkedList([])),
    (LinkedList([1]), LinkedList([1])),
    (LinkedList([1, 3, -1, 4]), LinkedList([4, -1, 3, 1])),
    (LinkedList([1, 2, 3, 4]), LinkedList([4, 3, 2, 1])),
    (LinkedList([1, 2, 3, 2, 1]), LinkedList([1, 2, 3, 2, 1])),
])
def test_cycled_linked_list(head, expected):
    assert reverse_linked_list(head) == expected
