# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        index = len(digits) - 1
        while index >= 0 and carry == 1:
            v = digits[index] + carry
            if v >= 10:
                carry = 1
                digits[index] = v % 10
            else:
                carry = 0
                digits[index] = v

            index -= 1

        if 1 == carry:
            digits.insert(0, carry)

        return digits
