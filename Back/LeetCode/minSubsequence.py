from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        for index in range(1, len(nums)):
            left = nums[:index]
            right = nums[index:]

            if sum(left) > sum(right):
                return left

        return nums
