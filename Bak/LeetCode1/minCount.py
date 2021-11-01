from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        result = 0

        for num in coins:
            result += num // 2
            if num % 2 > 0:
                result += 1

        return result