from typing import List

class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        reverse_list = list(reversed(cont))
        result = [reverse_list[0], 1]
        for i in range(1, len(cont)):
            num = reverse_list[i]
            element = num * result[0] + result[1]
            denominator = result[0]
            result[0] = element
            result[1] = denominator

        return result