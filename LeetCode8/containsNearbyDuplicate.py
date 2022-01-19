

# Given an integer array nums and an integer k, return true if there are
# two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 1):
            v, end = nums[i], min(i + k + 1, n)
            try:
                index = nums[i + 1: end].index(v)
                return True
            except ValueError:
                continue

        return False




