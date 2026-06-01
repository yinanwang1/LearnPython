from typing import List

# 2144. 打折购买糖果的最小开销
# https://leetcode.cn/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        l = len(cost)
        for i in range(0 ,l, 3):
            total += cost[i]
            if i + 1 < l:
                total += cost[i + 1]

        return total



