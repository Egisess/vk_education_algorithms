from sem2.linked_list import *


def cycled_list(head: Node) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


# test = LinkedList([1]).make_cycle([[0, 0]]).dummy_head

# print(test.data, test.next.data, test.next.next.data)
# print(cycled_list(LinkedList([1]).make_cycle([[0, 0]]).dummy_head))