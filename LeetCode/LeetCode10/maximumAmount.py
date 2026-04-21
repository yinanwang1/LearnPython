from linecache import cache
from math import inf
from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if i >= m or j >= n:
                return -inf

            x = coins[i][j]
            if i == m - 1 and j == n - 1:
                return max(0, x) if k > 0 else x

            res = max(dfs(i + 1, j, k), dfs(i, j + 1, k)) + x
            if k > 0 and x < 0:
                res = max(res, dfs(i + 1, j, k - 1), dfs(i, j + 1, k - 1))

            return res

        result = dfs(0, 0, 2)
        dfs.cache_clear()

        return result
