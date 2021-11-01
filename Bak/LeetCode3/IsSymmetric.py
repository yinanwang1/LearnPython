# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def reverse(left: TreeNode, right: TreeNode) -> bool:
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            else:
                return left.val == right.val and reverse(left.left, right.right) and reverse(left.right, right.left)

        return reverse(root, root)

