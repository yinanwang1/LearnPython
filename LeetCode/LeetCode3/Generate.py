from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if 0 == numRows:
            return []
        if 1 == numRows:
            return [[1]]

        result = [[1], [1, 1]]
        for _ in range(numRows - 2):
            temp = [1]
            lastList = result[-1] 

            for i in range(len(lastList) - 1):
                temp.append(lastList[i] + lastList[i + 1])

            temp.append(1)

            result.append(temp)

        return result
