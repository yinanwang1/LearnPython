from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i < j:
            while i < j and nums[i] % 2 == 1: i += 1
            while i < j and nums[j] % 2 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]


        return nums
