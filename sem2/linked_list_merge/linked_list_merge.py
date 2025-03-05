from sem2.linked_list import *


def linked_list_merge(A: LinkedList, B: LinkedList) -> LinkedList:
    head = A.dummy_head
    cur_a = A.dummy_head.next
    cur_b = B.dummy_head.next

    while cur_a and cur_b:
        if cur_a.data <= cur_b.data:
            head.next = cur_a
            cur_a = cur_a.next
            head = head.next
        else:
            head.next = cur_b
            cur_b = cur_b.next
            head = head.next

    if cur_a:
        head.next = cur_a
        cur_a = cur_a.next
        head = head.next
    if cur_b:
        head.next = cur_b
        cur_b = cur_b.next
        head = head.next

    return A


# A = LinkedList([1, 1, 3])
# B = LinkedList([2, 3, 4, 5, 6])
#
# print(linked_list_merge(A, B))
#
# A = LinkedList()
# B = LinkedList([2, 3, 4, 5, 6])
#
# print(linked_list_merge(A, B))
#
# A = LinkedList([1,2,3,4])
# B = LinkedList()
#
# print(linked_list_merge(A, B))