from cytoolz.itertoolz import deque


# Python 像JS一样支持一个变量多种类型
class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None



# 层序遍历
def level_order(root: TreeNode | None) -> list[int]:
    queue: deque[TreeNode] = deque()
    
    queue.append(root)

    res = []
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return res

res = []

# 前序遍历
def pre_order(root: TreeNode | None):
    if root is None:
        return
    res.append(root.val)
    pre_order(root.left)
    pre_order(root.right)

# 中序遍历
def in_order(root: TreeNode | None):
    if root is None:
        return
    in_order(root.left)
    res.append(root.val)
    in_order(root.right)

# 后序遍历
def post_order(root: TreeNode | None):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    res.append(root.val)



if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)
    node12 = TreeNode(12)
    node13 = TreeNode(13)
    node14 = TreeNode(14)
    node15 = TreeNode(15)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9
    node5.left = node10
    node5.right = node11
    node6.left = node12
    node6.right = node13
    node7.left = node14
    node7.right = node15

    result = level_order(node1)
    print(result)

    in_order(node1)
    print(res)

    res.clear()
    post_order(node1)
    print(res)





