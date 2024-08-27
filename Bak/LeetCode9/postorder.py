
# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal. Each group of children
# is separated by the null value (See examples)


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = list()

        def recursive(node: Node):
            if node is None:
                return
            if node.children is None:
                return

            for n in node.children:
                recursive(n)

            res.append(node.val)

        recursive(root)

        return res




