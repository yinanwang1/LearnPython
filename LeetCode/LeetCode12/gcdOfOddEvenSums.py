from math import gcd


# 3658. 奇数和与偶数和的最大公约数
# https://leetcode.cn/problems/gcd-of-odd-and-even-sums/description/


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = (1 + 2 * n - 1) * n // 2
        even = (2 + 2 * n) * n // 2
        return gcd(odd, even)
