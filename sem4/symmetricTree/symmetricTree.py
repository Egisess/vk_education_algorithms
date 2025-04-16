from sem4.symmetricTree import Node
def bfs(node: Node):
    if node is None:
        return True
    queue = [node]
    
    while len(queue) > 0:
        qlen = len(queue)
        for i in range(qlen):
            if queue[i] is None and queue[qlen - 1 - i] is None:
                continue
            elif queue[i] is None or queue[qlen - 1 - i] is None:
                return False
            elif queue[i].value != queue[qlen - 1 - i].value:
                return False
            queue.append(queue[i].left)
            queue.append(queue[i].right)
        queue = queue[qlen:]
    return True

def dfs(node: Node, res):
    if node is None:
        return res
    dfs(node.left, res)
    res.append(node.value)
    dfs(node.right, res)
    return res

def isSymmetric(node: Node):
    if node is None:
        return True
    res = dfs(node, res)
    for i in range(len(res) // 2):
        if res[i] != res[len(res) - 1 - i]:
            return False
    return True