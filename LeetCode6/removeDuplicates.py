from typing import List


# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        f = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[f]:
                f += 1
                nums[f] = nums[i]

        return f + 1

