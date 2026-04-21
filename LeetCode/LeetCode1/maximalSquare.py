from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        if 0 >= row:
            return 0
        column = len(matrix[0])

        result = set()

        def findSquare(i: int, j: int, times: int, area: int) -> int:
            columnTemp = j + times
            if columnTemp >= column:
                return area
            rowTemp = i + times
            if rowTemp >= row:
                return area

            for index in range(times + 1):
                if '1' != matrix[i + index][columnTemp]:
                    return area

                if '1' != matrix[rowTemp][j + index]:
                    return area

            return findSquare(i, j, times + 1, (times + 1) ** 2)

        for i in range(row):
            for j in range(column):
                if '1' == matrix[i][j]:
                    area = findSquare(i, j, 1, 1)
                    result.add(area)

        return max(result) if len(result) > 0 else 0





