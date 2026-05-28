from typing import List


# 3093. 最长公共后缀查询
# https://leetcode.cn/problems/longest-common-suffix-queries/


class Node:
    index: int
    character: str
    length: int
    next_nodes: dict[str, "Node"]

    def __init__(self, index: int, character: str, length: int):
        self.index = index
        self.character = character
        self.length = length
        self.next_nodes = {}


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        first_node_dic: dict[str, Node] = {}
        min_length = 10 ** 5
        min_length_index = 0
        for i, word in enumerate(wordsContainer):
            n = len(word)
            if n < min_length:
                min_length = n
                min_length_index = i
            nodes = first_node_dic
            for j in range(n-1, -1, -1):
                c = word[j]
                node = Node(i, c, n)
                if c not in nodes.keys():
                    nodes[c] = node
                    nodes = node.next_nodes
                    continue
                pre_node = nodes[c]
                if pre_node.length > n:
                    pre_node.index = i
                    pre_node.length = n
                nodes = pre_node.next_nodes

        ans = []
        for word in wordsQuery:
            nodes = first_node_dic
            index = min_length_index
            for j in range(len(word)-1, -1, -1):
                c = word[j]
                if c not in nodes.keys():
                    ans.append(index)
                    break
                pre_node = nodes[c]
                index = pre_node.index
                nodes = pre_node.next_nodes
            else:
                ans.append(index)

        return ans



if __name__ == '__main__':
    # print(Solution().stringIndices(wordsContainer=["abcd","bcd","xbcd"], wordsQuery=["cd","bcd","xyz"]))
    print(Solution().stringIndices(wordsContainer=["abcdefgh","poiuygh","ghghgh"], wordsQuery=["gh","acbfgh","acbfegh"]))