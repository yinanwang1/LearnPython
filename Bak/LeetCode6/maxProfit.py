from typing import List

# 给定一个数组 prices ，其中prices[i] 是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def f(index: int) -> (int, int):
            if 0 == index:
                return 0, -prices[0]

            a, b = f(index - 1)
            c = max(a, b + prices[index])
            d = max(b, a - prices[index])

            return c, d
        a, b = f(len(prices) - 1)

        return max(a, b)


