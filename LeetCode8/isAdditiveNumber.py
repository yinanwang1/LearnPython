# An additive number is a string whose digits can form an additive sequence.
# A valid additive sequence should contain at least three numbers. Except for
# the first two numbers, each subsequent number in the sequence must be the sum of
# the preceding two.
# Given a string containing only digits, return true if it is an additive number or
# false otherwise.
# Note: Numbers in the additive sequence cannot have leading zeros,
# so sequence 1, 2, 03 or 1, 02, 3 is invalid.
import math


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        lengthNum = len(num)
        if lengthNum < 3:
            return False

        m = 2 if '0' == num[0] else math.ceil(lengthNum / 2)
        for i in range(1, m):
            l = max(math.ceil((lengthNum - 2 * i) / 2), math.ceil((lengthNum - i) / 2)) + 1
            first = int(num[:i])
            for j in range(1, l):
                current = i + j
                second = num[i:current]
                if 1 < len(second) and '0' == second[0]:
                    break
                p = first
                q = int(second)
                while current < lengthNum:
                    s = p + q
                    lengthS = len(str(s))
                    if s == int(num[current: current + lengthS]):
                        current += lengthS
                        p = q
                        q = s
                    else:
                        break

                if current == lengthNum:
                    return True

        return False
