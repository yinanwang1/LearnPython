# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes: dict[int, TreeNode] = {}
        parents_keys = set()
        children_keys = set()
        for a, b, c in descriptions:
            node = nodes.get(a, None)
            if node is None:
                node = TreeNode(a)
                nodes[a] = node
            child = nodes.get(b, None)
            if child is None:
                child = TreeNode(b)
                nodes[b] = child
            if c == 1:
                node.left = child
            else:
                node.right = child

            parents_keys.add(a)
            children_keys.add(b)

        for key in children_keys:
            if key in parents_keys:
                parents_keys.remove(key)

        return nodes[parents_keys.pop()] if len(parents_keys) >= 1 else None


if __name__ == '__main__':
    print(Solution().createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))
