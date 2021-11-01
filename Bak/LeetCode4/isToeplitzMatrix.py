from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = [0, n-1]

        while True:
            x = start[0]
            y = start[1]
            if y > 0:
                y -= 1
                x = 0
            else:
                x += 1
                y = 0
            start.clear()
            start.append(x)
            start.append(y)

            if x >= m:
                break

            value = matrix[x][y]
            while True:
                x += 1
                y += 1

                if x >= m or y >= n:
                    break

                if value != matrix[x][y]:
                    return False

        return True
