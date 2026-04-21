from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for nums in accounts:
            result = max(result, sum(nums))

        return result