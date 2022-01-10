# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
# A divisor of an integer x is an integer that can divide x evenly.
# Given an integer n, return true if n is a perfect number, otherwise return false.
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if 1 == num:
            return False

        right = math.sqrt(num)
        result = 0 if right != math.ceil(right) else math.ceil(right)
        for i in range(1, math.ceil(right)):
            if num % i == 0:
                result += i
                result += num // i

        return num == result



