from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        resultList = list(map(lambda x: x * x, A))
        resultList.sort()

        return resultList