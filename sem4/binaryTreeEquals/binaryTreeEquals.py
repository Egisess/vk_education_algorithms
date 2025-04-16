from sem4.treeNode import Node
def binaryTreeEquals(node1: Node, node2: Node):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.value != node2.value:
        return False
    return (binaryTreeEquals(node1.right, node2.left)
             and binaryTreeEquals(node1.left, node2.right))
    
