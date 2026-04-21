# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def recursion(node: TreeNode):
            if node is None:
                return None
            elif node.val < low:
                return recursion(node.right)
            elif node.val > high:
                return recursion(node.left)
            else:
                node.left = recursion(node.left)
                node.right = recursion(node.right)
                return node

        return recursion(root)

