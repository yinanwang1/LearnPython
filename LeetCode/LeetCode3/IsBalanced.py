# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def recursion(node: TreeNode) -> bool:
            if node is None:
                return True

            if node.left is not None and node.right is not None:
                result1 = recursion(node.left)
                result2 = recursion(node.right)
                if result1 and result2 and abs(node.left.val - node.right.val) <= 1:
                    node.val = max(node.left.val, node.right.val) + 1
                    return True
                else:
                    return False
            elif node.left is not None:
                result = recursion(node.left)
                print("result is {}, node.left.val is {}".format(result, node.left.val))
                if result and node.left.val <= 0:
                    node.val = 1
                    return True
                else:
                    return False

            elif node.right is not None:
                result = recursion(node.right)
                if result and node.right.val <= 0:
                    node.val = 1
                    return True
                else:
                    return False
            else:
                node.val = 0
                return True

        return recursion(root)



