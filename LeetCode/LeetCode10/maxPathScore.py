from functools import cache
from math import inf
from typing import List


# 3742. 网格中得分最大的路径
# https://leetcode.cn/problems/maximum-path-score-in-a-grid/description/

# 使用了
# @cache
# dfs.cache_clear()
# 来解决缓存问题，解决内存超出限制的问题

max = lambda a, b: b if b > a else a
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        @cache
        def dfs(i, j, c):
            if i < 0 or j < 0 or c < 0:
                return -inf
            score = grid[i][j]
            cost = 0 if 0 == grid[i][j] else 1
            if i == 0 and j == 0:
                return 0
            return max(dfs(i - 1, j,c - cost), dfs(i,j - 1,c - cost)) + score

        res = dfs(m - 1, n - 1, k)
        dfs.cache_clear()
        return -1 if res < 0 else res


if __name__ == '__main__':
    # print(Solution().maxPathScore(grid=[[0, 1], [2, 0]], k=1))
    print(Solution().maxPathScore(grid=[[0, 0, 2],[0, 1, 0],[2, 0, 2]], k=4))
    # print(Solution().maxPathScore(grid=[[0, 1], [1, 2]], k=1))
    # print(Solution().maxPathScore(grid=[[0]], k=0))
