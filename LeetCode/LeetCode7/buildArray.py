# Given a zero-based permutation nums (0-indexed),
# build an array ans of the same length where
# ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers
# from 0 to nums.length - 1 (inclusive).


from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * l
        for i in range(l):
            ans[i] = nums[nums[i]]

        return ans