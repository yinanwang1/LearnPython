

# Given a 0-indexed integer array nums, find the leftmost middleIndex
# (i.e., the smallest amongst all the possible ones).
# A middleIndex is an index where nums[0] + nums[1] + ...
# + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
# If middleIndex == 0, the left side sum is considered to be 0. Similarly,
# if middleIndex == nums.length - 1, the right side sum is considered to be 0.
# Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for i, v in enumerate(nums):
            right -= v
            if left == right:
                return i
            left += v
        else:
            return -1
