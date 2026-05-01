from typing import List

# 396. 旋转函数
# https://leetcode.cn/problems/rotate-function/description/

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        l = len(nums)
        total = sum(nums)
        f = sum([i * num for i, num in enumerate(nums)])
        result = f
        for num in nums[::-1]:
            f = f + total - l * num
            result = max(result, f)

        return  result
