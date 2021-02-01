from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = list()

        def recursion(path: List[List[str]]):
            if n == len(path):
                result.append(path)
                return

            row = len(path)
            for i in range(n):
                exist = False
                for j in range(1, row+1):
                    if 0 <= row - j and 'Q' == path[row - j][i]:
                        exist = True
                        break
                    if 0 <= row - j and 0 <= i - 1 and 'Q' == path[row - j][i - 1]:
                        exist = True
                        break

                    if 0 <= row - j and i + 1 < n and 'Q' == path[row - j][i + 1]:
                        exist = True
                        break

                if not exist:
                    rowTemp = ['.'] * n
                    rowTemp[i] = 'Q'
                    pathTemp = path.copy()
                    pathTemp.append(rowTemp)
                    recursion(pathTemp)

        for i in range(n):
            row = ['.'] * n
            row[i] = 'Q'
            recursion([row])

        return [[''.join(row) for row in table] for table in result]