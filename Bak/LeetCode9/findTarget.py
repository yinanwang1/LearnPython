# 给定一个二叉搜索树的 根节点 root 和一个整数 k ,
# 请判断该二叉搜索树中是否存在两个节点它们的值之和等于 k 。假设二叉搜索树中节点的值均唯一。


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.nums = []

    def findTarget(self, root: TreeNode, k: int) -> bool:
        def recurse(node: TreeNode):
            if node is None:
                return
            recurse(node.left)
            self.nums.append(node.val)
            recurse(node.right)

        recurse(root)
        left, right = 0, len(self.nums) - 1
        res = False
        while left < right:
            temp = self.nums[left] + self.nums[right]
            if temp == k:
                res = True
                break
            elif temp < k:
                left += 1
            else:
                right -= 1

        return res







