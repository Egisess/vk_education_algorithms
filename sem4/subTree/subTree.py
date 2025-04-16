from sem4.binaryTreeEquals import binaryTreeEquals
from sem4.treeNode import Node
def subTree(a: Node, b: Node):
    if not b:
        return True
    if not a:
        return False
    if binaryTreeEquals(a, b):
        return True
    return subTree(a.left, b) or subTree(a.right, b)
