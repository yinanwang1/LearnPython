# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.result = None
        self.current = None

        def traverse(node: TreeNode):
            if node.left is not None:
                traverse(node.left)

            if self.result is None:
                self.result = TreeNode(node.val)
                self.current = self.result
            else:
                self.current.right = TreeNode(node.val)
                self.current = self.current.right

            if node.right is not None:
                traverse(node.right)

        traverse(root)

        return self.result