# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def traverse(l: TreeNode, r: TreeNode) -> bool:
            if l is None and r is None:
                return True
            elif l is None or r is None:
                return False

            if l.val != r.val:
                return False

            result = traverse(l.left, r.left)
            if result is False:
                return False
            result = traverse(l.right, r.right)
            if result is False:
                return False

            return True

        return traverse(p, q)




