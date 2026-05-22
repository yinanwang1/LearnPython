from typing import List

# 33. 搜索旋转排序数组
# https://leetcode.cn/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v == target:
                return i
        else:
            return -1
