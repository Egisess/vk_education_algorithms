import pytest
from middle_linked_list import middle_linked_list
from sem2.linked_list import *

test_1 = LinkedList([1, 2, 3, 4, 5])
test_2 = LinkedList([1, 2, 3, 4])
test_3 = LinkedList([1])
test_4 = LinkedList([1, 2])
test_5 = LinkedList()


@pytest.mark.parametrize("head, expected", [
    (test_1, test_1.get_i_th_node(2)),
    (test_2, test_2.get_i_th_node(2)),
    (test_3, test_3.get_i_th_node(0)),
    (test_4, test_4.get_i_th_node(1)),
    (test_5, None),
])
def test_cycled_linked_list(head, expected):
    assert middle_linked_list(head) == expected
