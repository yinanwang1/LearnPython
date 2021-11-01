# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.firstNode = self.head = TreeNode(-1)

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def recurse(node: TreeNode):
            if not node:
                return

            recurse(node.left)

            node.left = None
            self.firstNode.right = node
            self.firstNode = node

            recurse(node.right)

        recurse(root)

        return self.head.right
