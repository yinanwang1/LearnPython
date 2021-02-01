# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []

        def recursion(node: TreeNode, path: str):
            if node is None:
                return

            path += str(node.val)
            if node.left is None and node.right is None:
                paths.append(path)
            else:
                path += '->'
                recursion(node.left, path)
                recursion(node.right, path)

        recursion(root, '')

        return paths
