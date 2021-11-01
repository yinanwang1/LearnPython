from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = nums[0]
        pre = nums[0]
        for i in range(1, len(nums)):
            pre = max(nums[i], nums[i] + pre)
            maxValue = max(maxValue, pre)

        return maxValue
