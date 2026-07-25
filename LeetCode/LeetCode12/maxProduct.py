
# 3536. 两个数字的最大乘积
# https://leetcode.cn/problems/maximum-product-of-two-digits/



class Solution:
    def maxProduct(self, n: int) -> int:
        nums = []
        temp = n
        while temp > 0:
            nums.append(temp % 10)
            temp = temp // 10
        nums.sort()

        return nums[-1] * nums[-2]

