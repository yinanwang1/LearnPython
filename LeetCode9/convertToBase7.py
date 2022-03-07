
# Given an integer num, return a string of its base 7 representation.

class Solution:
    def convertToBase7(self, num: int) -> str:
        result, positive, temp = "", num > 0, abs(num)
        while temp > 0:
            result = str(temp % 7) + result
            temp //= 7

        return result if positive else "-" + result

