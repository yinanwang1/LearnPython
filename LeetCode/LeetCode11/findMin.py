from typing import List


# 153. 寻找旋转排序数组中的最小值
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        value = nums[0]
        for i, v in enumerate(nums, start=1):
            if v < value:
                return v
        else:
            return value

