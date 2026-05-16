from typing import List

# 154. 寻找旋转排序数组中的最小值 II
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/description/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        value = nums[0]
        for i, v in enumerate(nums, start=1):
            if v < value:
                return v

        return value


