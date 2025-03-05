from sem2.linked_list import *


def linked_list_delete(head: LinkedList, val):
    prev = head.dummy_head
    cur = prev.next

    while cur:
        if cur.data == val:
            prev.next = cur.next
            break
        cur = cur.next
        prev = prev.next

    return head

test = LinkedList([1, 2, 3, 4])
print(linked_list_delete(test, 3))

test = LinkedList([])
print(linked_list_delete(test, 3))