from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += digits[-1] + 1
            return digits

        num = ''
        for i in digits:
            num += str(i)
        value = int(num) + 1
        result = list()
        for char in str(value):
            result.append(int(char))

        return result
