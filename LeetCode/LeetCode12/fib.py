from functools import cache


# LCR 126. 斐波那契数
# https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/description/

class Solution:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def fib(n) -> int:
            if 0 == n:
                return 0
            if 1 == n:
                return 1
            return fib(n - 1) + fib(n - 2)

        return fib(n) % MOD

