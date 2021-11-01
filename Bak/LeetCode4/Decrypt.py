from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        result = list()
        for i in range(len(code)):
            index = i
            value = 0
            for time in range(abs(k)):
                if k > 0:
                    index += 1
                    if index >= len(code):
                        index = 0
                else:
                    index -= 1
                    if index < 0:
                        index = len(code) - 1
                value += code[index]
            result.append(value)

        return result


