# Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
#
# x mod y denotes the remainder when x is divided by y.


from typing import List

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if v == i % 10:
                return i

        return -1

