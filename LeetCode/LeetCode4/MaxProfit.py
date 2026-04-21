from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0
        dp1 = -prices[0]
        for index in range(1, len(prices)):
            dp0Temp = max(dp0, dp1 + prices[index])
            dp1Temp = max(dp1, dp0 - prices[index])
            dp0 = dp0Temp
            dp1 = dp1Temp

        return dp0
