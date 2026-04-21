# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

from typing import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = 0
        e = 0
        for n in nums:
            if n < target:
                l += 1
            elif n == target:
                e += 1

        return list(range(l, e + l))


