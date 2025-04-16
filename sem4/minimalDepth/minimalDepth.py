from sem4.treeNode import Node

def minimalDepth(node: Node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    if node.left is None:
        return minimalDepth(node.right) + 1
    if node.right is None:
        return minimalDepth(node.left) + 1
    return min(minimalDepth(node.left), minimalDepth(node.right)) + 1