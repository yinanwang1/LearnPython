
# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
#
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].


from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = list()
        for i in range(left, right + 1):
            if self.divide(i):
                res.append(i)

        return res

    def divide(self, value: int) -> bool:
        values = list(str(value))
        for v in values:
            if 0 == int(v):
                return False

            if value % int(v) != 0:
                return False

        return True
