from sem4.treeNode import Node
from collections import deque
def kMinElement(root: Node, k: int):
    dq = deque()
    cnt = 0
    cur = root
    
    while len(dq) > 0 or cur:
        while cur:
            dq.append(cur)
            cur = cur.left
        cur = dq.pop()
        cnt += 1

        if cnt == k:
            return cur.value
        
        cur = cur.right
    return None

def kMaxElement(root: Node, k: int):
    dq = deque()
    cnt = 0
    cur = root
    
    while len(dq) > 0 or cur:
        while cur:
            dq.append(cur)
            cur = cur.right
        cur = dq.pop()
        cnt += 1

        if cnt == k:
            return cur.value
        
        cur = cur.left
    return None