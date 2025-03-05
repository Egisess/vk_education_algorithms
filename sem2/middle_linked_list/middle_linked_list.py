from sem2.linked_list import *
def middle_linked_list(head : LinkedList) -> Node:
    dummy = head.dummy_head
    slow = fast = dummy.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# test = LinkedList([1,2,3,4,5])
# print(middle_linked_list(test).data)
#
# test = LinkedList([1, 2, 3, 4])
# print(middle_linked_list(test).data)