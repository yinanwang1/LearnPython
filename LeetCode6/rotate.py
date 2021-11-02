# 给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。
#
# 进阶：
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 你可以使用空间复杂度为O(1) 的原地算法解决这个问题吗？

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # 倒序
        nums.reverse()
        print(nums)
        for i in range(k // 2):
            t = nums[i]
            nums[i] = nums[k - i - 1]
            nums[k - i - 1] = t

        print(nums)
        l = len(nums)
        for i in range(k, 1 + (l + k - 1) // 2):
            t = nums[i]
            nums[i] = nums[l - i - 1 + k]
            nums[l - i - 1 + k] = t

        print(nums)

