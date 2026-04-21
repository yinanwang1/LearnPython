import collections
from typing import List


# 1722. 执行交换操作后的最小汉明距离
# https://leetcode.cn/problems/minimize-hamming-distance-after-swap-operations/solutions/3956011/bing-cha-ji-pou-xi-wen-ti-ben-zhi-lian-t-lh1d/?envType=daily-question&envId=2026-04-21&status=NOT_STARTED&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJBQ19SQVRFIn1d&difficulty=EASY


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        # 路径压缩：直接指向根节点

        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        # 允许交换的下标进行连通
        for a, b in allowedSwaps:
            uf.union(a, b)

        # 按连根节点对下标进行分组
        groups = collections.defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        matches = 0

        # 遍历每一个连通分量
        for root, indices in groups.items():
            # 统计当前分量中 source 里的元素频率
            cnts = collections.Counter()
            for idx in indices:
                cnts[source[idx]] += 1

            # target 里的元素有多少能在 source 中找到匹配
            match_in_group = 0
            for idx in indices:
                val = target[idx]
                if cnts[val] > 0:
                    match_in_group += 1
                    cnts[val] -= 1

            matches += match_in_group

        # 总长度 - 总匹配数
        return n - matches


if __name__ == '__main__':
    # print(Solution().minimumHammingDistance([5,1,2,4,3], [1,5,4,2,3], [[0,4],[4,2],[1,3],[1,4]]))
    print(Solution().minimumHammingDistance([1, 2, 3, 4], [1, 3, 2, 4], []))
    # print(Solution().minimumHammingDistance([50,46,54,35,18,42,26,72,75,47,50,4,54,21,18,18,61,64,100,14],
    #                                         [83,34,43,73,61,94,10,68,74,31,54,46,28,60,18,18,4,44,79,92],
    #                                         [[1,8],[14,17],[3,1],[17,10],[18,2],[7,12],[11,3],[1,15],[13,17],[18,19],[0,10],[15,19],[0,15],[6,7],[7,15],[19,4],[7,16],[14,18],[8,10],[17,0],[2,13],[14,10],[12,17],[2,9],[6,15],[16,18],[2,16],[2,6],[4,5],[17,5],[10,13],[7,2],[9,16],[15,5],[0,5],[8,0],[11,12],[9,7],[1,0],[11,17],[4,6],[5,7],[19,12],[3,18],[19,1],[13,18],[19,6],[13,6],[6,1],[4,2]]))
