from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        indexSet = []
        length = len(mat)

        for i in range(0, length):
            indexSet.append((i, i))
            result += mat[i][i]

            try:
                indexSet.index((length - 1 - i, i))
            except:
                indexSet.append((length - 1 - i, i))
                result += mat[length - 1 - i][i]

        return result



