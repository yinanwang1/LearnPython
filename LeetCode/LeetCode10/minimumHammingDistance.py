from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.fa[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        for a, b in allowedSwaps:
            uf.union(a, b)

        sets = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            f = uf.find(i)
            sets[f][source[i]] += 1

        ans = 0
        for i in range(n):
            f = uf.find(i)
            if sets[f][target[i]] > 0:
                sets[f][target[i]] -= 1
            else:
                ans += 1
        return ans



if __name__ == '__main__':
    print(Solution().minimumHammingDistance([5,1,2,4,3], [1,5,4,2,3], [[0,4],[4,2],[1,3],[1,4]]))
    # print(Solution().minimumHammingDistance([50,46,54,35,18,42,26,72,75,47,50,4,54,21,18,18,61,64,100,14],
    #                                         [83,34,43,73,61,94,10,68,74,31,54,46,28,60,18,18,4,44,79,92],
    #                                         [[1,8],[14,17],[3,1],[17,10],[18,2],[7,12],[11,3],[1,15],[13,17],[18,19],[0,10],[15,19],[0,15],[6,7],[7,15],[19,4],[7,16],[14,18],[8,10],[17,0],[2,13],[14,10],[12,17],[2,9],[6,15],[16,18],[2,16],[2,6],[4,5],[17,5],[10,13],[7,2],[9,16],[15,5],[0,5],[8,0],[11,12],[9,7],[1,0],[11,17],[4,6],[5,7],[19,12],[3,18],[19,1],[13,18],[19,6],[13,6],[6,1],[4,2]]))
