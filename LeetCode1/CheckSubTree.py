# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = False

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def same(node1: TreeNode, node2: TreeNode) -> bool:
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None or node1.val != node2.val:
                return False

            if not same(node1.left, node2.left):
                return False

            if not same(node1.right, node2.right):
                return False

            return True

        def recursion(node: TreeNode):
            if node is None or self.result:
                return

            if same(node, t2):
                self.result = True
                return

            recursion(node.left)
            recursion(node.right)

        recursion(t1)

        return self.result


