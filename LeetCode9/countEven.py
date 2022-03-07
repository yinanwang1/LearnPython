
# Given a positive integer num, return the number of positive integers
# less than or equal to num whose digit sums are even.
#
# The digit sum of a positive integer is the sum of all its digits.

class Solution:
    def countEven(self, num: int) -> int:
        def calc(v: int) -> int:
            res, vStr = 0, str(v)
            for s in vStr:
                res += int(s)
            return res

        result = 0
        for i in range(2, num+1):
            res = calc(i)
            if res % 2 == 0:
                result += 1

        return result


