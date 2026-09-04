


# 3876. 构造奇偶一致的数组 II
# https://leetcode.cn/problems/construct-uniform-parity-array-ii/description/

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_value = 10 ** 9 + 1
        odd_total = 0
        for num in nums1:
            if num % 2 == 1:
                odd_total += 1
            min_value = min(min_value, num)
        if 0 == odd_total or odd_total == len(nums1) or 1 == min_value % 2:
            return True

        return False



