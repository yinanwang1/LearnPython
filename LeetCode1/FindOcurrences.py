from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        chars = text.split(' ')
        result = list()
        for i in range(2, len(chars)):
            if chars[i - 2] == first and chars[i - 1] == second:
                result.append(chars[i])

        return result
