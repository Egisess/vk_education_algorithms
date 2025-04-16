from collections import deque
from sem4.treeNode import Node
def fullBinaryTree(node: Node):
    if not node:
        return True
    
    q = deque(node)
    isLeaf = False

    while len(q) > 0
        cur = q.popleft()

        if not cur:
            isLeaf = True
        else:
            if isLeaf:
                return False
            q.append(cur.left)
            q.append(cur.right)
    return True
