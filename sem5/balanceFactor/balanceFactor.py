# Balance factor - разница высот левого и правого поддерева (левое - правое)
from sem4.treeNode import Node
def heightsAndBalance(root):
    if not root:
        return 0
    
    leftH = heightsAndBalance(root.left)
    rightH = heightsAndBalance(root.right)

    root.balanceFactor = leftH - rightH

    return 1 + max(leftH, rightH)

