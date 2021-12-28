# 「力扣挑战赛」开幕式开始了，空中绽放了一颗二叉树形的巨型焰火。
# 给定一棵二叉树 root 代表焰火，节点值表示巨型焰火这一位置的颜色种类。请帮小扣计算巨型焰火有多少种不同的颜色。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numColor(self, root: TreeNode) -> int:
        colors = {root.val}

        def recurseNode(node: TreeNode):
            if node is None:
                return
            if node.left is not None:
                colors.add(node.left.val)
                recurseNode(node.left)
            if node.right is not None:
                colors.add(node.right.val)
                recurseNode(node.right)

        recurseNode(root)

        return len(colors)

