from sem4.treeNode import Node

def treeRestore(nums: list, start: int) -> Node:
    if start >= len(nums):
        return None
    root = Node(nums[start])
    root.left = treeRestore(nums, 2*start + 1)
    root.right = treeRestore(nums, 2*start + 2)
    return root

    