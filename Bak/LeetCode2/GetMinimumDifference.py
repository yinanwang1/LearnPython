# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution:
    def __init__(self):
        self.miniNum = sys.maxsize
        self.preNum = sys.maxsize

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.traverse(root)

        return self.miniNum

    def traverse(self, current: TreeNode):
        if current.left is not None:
            self.traverse(current.left)

        if self.preNum == sys.maxsize:
            self.preNum = current.val
        else:
            self.miniNum = min(self.miniNum, current.val - self.preNum)
            self.preNum = current.val

        if current.right is not None:
            self.traverse(current.right)


