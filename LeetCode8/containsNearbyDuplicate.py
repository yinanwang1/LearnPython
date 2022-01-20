# Given an integer array nums and an integer k, return true if there are
# two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numIndex = {}
        for i in range(len(nums)):
            v = nums[i]
            if numIndex.keys().__contains__(v) and i - numIndex[v] <= k:
                return True
            numIndex[v] = i

        return False
