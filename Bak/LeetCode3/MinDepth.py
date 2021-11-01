# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        deep = 1
        nodeList = [root]

        while len(nodeList) > 0:
            tempNodeList = list()
            for node in nodeList:
                if node.left is None and node.right is None:
                    return deep
                elif node.left is None:
                    tempNodeList.append(node.right)
                elif node.right is None:
                    tempNodeList.append(node.left)
                else:
                    tempNodeList.append(node.left)
                    tempNodeList.append(node.right)

            nodeList = tempNodeList
            deep += 1

        return deep
