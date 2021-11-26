# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
#
# 假设环境不允许存储 64 位整数（有符号或无符号）。

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        while x != 0:
            if res < INT_MIN // 10 + 1 or res > INT_MAX // 10:
                return 0
            d = x % 10
            if x < 0 and d > 0:
                d -= 10
            x = (x - d) // 10
            res = res * 10 + d

        return res
