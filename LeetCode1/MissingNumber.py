from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = int(len(nums) * (len(nums) + 1) / 2)
        return total - sum(nums)
