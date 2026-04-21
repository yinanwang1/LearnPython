# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_new = sorted(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            v = nums_new[l] + nums_new[r]
            if v == target:
                index_l = nums.index(nums_new[l])
                index_r = nums.index(nums_new[r])
                if index_r == index_l:
                    index_r += 1
                    index_r += nums[index_r:].index(nums_new[r])

                return [index_l, index_r]
            elif v < target:
                l += 1
            else:
                r -= 1

        return []


