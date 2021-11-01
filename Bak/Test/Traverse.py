class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)

root.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)
root.left.left.right.left = TreeNode(7)
root.left.left.right.right = TreeNode(8)


class Traverse:
    # 先序
    def preorderTraversal(self):
        nums = []

        def traversal(node: TreeNode):
            if node is None:
                return
            nums.append(node.val)

            if node.left is not None:
                traversal(node.left)

            if node.right is not None:
                traversal(node.right)

        traversal(root)
        print(nums)

    # 中序
    def inorderTraversal(self):
        nums = []

        def traversal(node: TreeNode):
            if node is None:
                return

            if node.left is not None:
                traversal(node.left)

            nums.append(node.val)

            if node.right is not None:
                traversal(node.right)

        traversal(root)
        print(nums)

    # 后序
    def postorderTraversal(self):
        nums = []

        def traversal(node: TreeNode):
            if node is None:
                return

            if node.left is not None:
                traversal(node.left)

            if node.right is not None:
                traversal(node.right)

            nums.append(node.val)

        traversal(root)
        print(nums)


traverse = Traverse()

print('先序')
traverse.preorderTraversal()
print('中序')
traverse.inorderTraversal()
print('后序')
traverse.postorderTraversal()