from typing import List


# 153. 寻找旋转排序数组中的最小值
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

