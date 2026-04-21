# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursion(node: TreeNode, result: bool) -> (bool, list):
            if result is False:
                return result, list()

            if node is None:
                return result, list()

            if node.left is None:
                leftResult, leftNodeList = True, list()
            else:
                leftResult, leftNodeList = recursion(node.left, result)

            if node.right is None:
                rightResult, rightNodeList = True, list()
            else:
                rightResult, rightNodeList = recursion(node.right, result)

            if leftResult is False or rightResult is False:
                return False, list()

            print("leftNodeList is " + str(leftNodeList))
            print("rightNodeList is " + str(rightNodeList))

            matchLeft = True
            if len(leftNodeList) > 0:
                if max(leftNodeList) >= node.val:
                    matchLeft = False

            matchRight = True
            if len(rightNodeList) > 0:
                if node.val >= min(rightNodeList):
                    matchRight = False

            if matchLeft and matchRight:
                leftNodeList.append(node.val)
                return True, leftNodeList + rightNodeList

            return False, list()

        result, _ = recursion(root, True)

        return result
