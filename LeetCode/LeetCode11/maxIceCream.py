from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                ans += 1
            else:
                break
        return ans

