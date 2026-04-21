# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def recurse(node: TreeNode):
            if node:
                if not node.left and not node.right:
                    yield node.val

                yield from recurse(node.left)
                yield from recurse(node.right)

        return list(recurse(root1)) == list(recurse(root2))


