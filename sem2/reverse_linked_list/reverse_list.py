from sem2.linked_list import *


def reverse_linked_list(head: LinkedList) -> LinkedList:
    dummy = head.dummy_head
    cur = dummy.next
    prev = None

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    dummy.next = prev
    return head


# head = LinkedList([1, 2, 3, 4])
# print(reverse_linked_list(head))
