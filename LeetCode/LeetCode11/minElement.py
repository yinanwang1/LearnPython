from typing import List


# 3300. 替换为数位和以后的最小元素
# https://leetcode.cn/problems/minimum-element-after-replacement-with-digit-sum/description/


class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 10 ** 4
        for num in nums:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            ans = min(total, ans)

        return ans




