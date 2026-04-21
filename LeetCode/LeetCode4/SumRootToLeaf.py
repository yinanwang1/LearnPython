# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.ans = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:

        def recursion(node: TreeNode, cur: int) -> int:
            if node is None:
                return 0

            if node.left is None and node.right is None:
                self.ans += cur * 2 + node.val

                return self.ans

            recursion(node.left, cur * 2 + node.val)
            recursion(node.right, cur * 2 + node.val)

        return recursion(root, 0)


