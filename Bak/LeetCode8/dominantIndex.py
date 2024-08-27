
# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as
# every other number in the array.
# If it is, return the index of the largest element, or return -1 otherwise.

from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if 1 == len(nums):
            return 0
        t = sorted(nums)
        if t[-1] < t[-2] * 2:
            return -1
        return nums.index(t[-1])

