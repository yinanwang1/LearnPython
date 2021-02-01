from typing import List

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for t in range(0, k):
            dpTemp = [0] * (n + 1)
            for x, y in relation:
                dpTemp[y] += dp[x]

            dp = dpTemp

        return dp[n-1]