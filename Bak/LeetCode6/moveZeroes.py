
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hasZero = False
        zeroIndex = 0
        for i in range(len(nums)):
            v = nums[i]
            if 0 == v:
                if hasZero:
                    continue
                else:
                    hasZero = True
                    zeroIndex = i
            else:
                if hasZero:
                    nums[zeroIndex] = v
                    nums[i] = 0
                    zeroIndex += 1
