from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        total = len(nums)
        while index < total:
            if 0 == nums[index]:
                nums.pop(index)
                nums.append(0)
                total -= 1
                continue
            index += 1


