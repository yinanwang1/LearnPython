# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
#
# The value of |x| is defined as:
#
# x if x >= 0.
# -x if x < 0.

from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if k == abs(nums[i] - nums[j]):
                    count += 1

        return count
