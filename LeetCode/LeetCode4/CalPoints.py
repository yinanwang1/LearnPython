from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = list()
        for value in ops:
            if value == 'C':
                result.pop()
            elif value == 'D':
                result.append(result[-1] * 2)
            elif value == '+':
                result.append(result[-1] + result[-2])
            else:
                result.append(int(value))

            print(result)

        return sum(result)