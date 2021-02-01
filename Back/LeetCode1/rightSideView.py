from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        rowNode = [root]
        result = [root.val]

        while len(rowNode) > 0:
            rowNodeTemp = list()
            for node in rowNode:
                if node is not None:
                    if node.left is not None:
                        rowNodeTemp.append(node.left)
                    if node.right is not None:
                        rowNodeTemp.append(node.right)
            if len(rowNodeTemp) > 0:
                result.append(rowNodeTemp[-1].val)
            rowNode = rowNodeTemp

        return result