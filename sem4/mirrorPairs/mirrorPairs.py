from sem4.treeNode import Node
def dfs(left: Node, right: Node):
    if not left or not right:
        return 0
    
    cnt = 0
    if left.value == right.value:
        cnt = 1
    
    cnt += dfs(left.left, right.right)
    cnt += dfs(left.right, right.left)
    return cnt

def MirrorPairs(root):
    if root:
        return 0
    
    return dfs(root.left, root.right)