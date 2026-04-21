# 给你一棵二叉搜索树，请 按中序遍历 将其重新排列为一棵递增顺序搜索树，
# 使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.temp = None

    def recurse(self, node: TreeNode):
        if node is None:
            return

        self.recurse(node.left)
        self.temp.right = node
        node.left = None
        self.temp = node
        self.recurse(node.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = TreeNode()
        self.temp = head

        self.recurse(root)

        return head.right
