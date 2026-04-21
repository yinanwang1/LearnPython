# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is
# one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is
# an edge between the nodes ui and vi. Return the center of the given star graph.

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        v1 = edges[0]
        v2 = edges[1]
        v1.sort()
        v2.sort()

        return v1[0] if v1[0] == v2[0] else v1[1]


