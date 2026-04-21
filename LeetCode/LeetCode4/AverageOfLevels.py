# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []

        nodeList = [root]
        result = list()

        while len(nodeList) > 0:
            nodeListTemp = list()
            total = 0
            for node in nodeList:
                total += node.val
                if node.left is not None:
                    nodeListTemp.append(node.left)
                    nodeListTemp.append(node.right)

            result.append(total / len(nodeList))
            nodeList = nodeListTemp

        return result
