from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return list(list())

        result = list()
        nodeList = [root]


        while len(nodeList) > 0:
            nodeListTemp = list()
            levelValueList = list()
            for node in nodeList:
                levelValueList.append(node.val)
                if node.left is not None:
                    nodeListTemp.append(node.left)
                if node.right is not None:
                    nodeListTemp.append(node.right)

            result.append(levelValueList)
            nodeList = nodeListTemp

        result.reverse()

        return result