from typing import List


# 3689. 最大子数组总值 I
# https://leetcode.cn/problems/maximum-total-subarray-value-i/description/


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))
