from sem4.treeNode import Node
def mirroring(root: Node):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    
    mirroring(root.left)
    mirroring(root.right)

    return root