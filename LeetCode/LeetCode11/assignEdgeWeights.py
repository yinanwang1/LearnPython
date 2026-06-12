from typing import List


# 3558. 给边赋权值的方案数 I
# https://leetcode.cn/problems/number-of-ways-to-assign-edge-weights-i/description/

class Node:
    def __init__(self, val):
        self.val = val
        self.children:List[Node] = []


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        nodes = {}
        node_children_set = set()
        for parent, child in edges:
            if parent not in nodes:
                nodes[parent] = Node(parent)
            if child not in nodes:
                nodes[child] = Node(child)

            nodes[parent].children.append(nodes[child])
            node_children_set.add(child)

        roots = [node for val, node in nodes.items() if val not in node_children_set]
        root = roots[0] if roots else None
        if root is None:
            return 1

        deep = -1
        node_list = [root]
        while len(node_list) > 0:
            deep += 1
            temp = []
            for node in node_list:
                temp += node.children
            node_list = temp

        return pow(2, deep - 1, 10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().assignEdgeWeights([[1, 2]]))
