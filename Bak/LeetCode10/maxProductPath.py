from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[1] * 2 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = dp[0][0][1] = grid[0][0]
        # 第一列
        for i in range(1, m):
            dp[i][0][0] = dp[i][0][1] = dp[i - 1][0][1] * grid[i][0]
        # 第一行
        for j in range(1, n):
            dp[0][j][0] = dp[0][j][1] = dp[0][j - 1][1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                if val >= 0:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0]) * val
                    dp[i][j][1] = min(dp[i - 1][j][1], dp[i][j - 1][1]) * val
                else:
                    dp[i][j][0] = min(dp[i - 1][j][1], dp[i][j - 1][1]) * val
                    dp[i][j][1] = max(dp[i - 1][j][0], dp[i][j - 1][0]) * val

        ma = dp[m - 1][n - 1][0]

        return -1 if ma < 0 else ma % (10 ** 9 + 7)
