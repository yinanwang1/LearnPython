from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        if 0 >= len(nums):
            return 0

        if 1 == len(nums):
            return nums[0]

        dp = [0] * len(nums)
        dp.append(nums[0])
        dp[1] = max(nums[0], nums[1])
        index = 2
        for index in range(2, len(nums)):
            dp[index] = max(dp[index - 1], dp[index - 2] + nums[index])

        return dp[index - 1]




# [4,1,2,7,5,3,1]】
