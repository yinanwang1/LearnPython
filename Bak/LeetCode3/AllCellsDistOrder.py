from typing import List
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = [[r0, c0]]
        pointList = [[r0, c0]]
        value1 = [-1, 0, 1, 0]
        value2 = [0, -1, 0, 1]
        valueMap = [[0] * C for _ in range(R)]
        valueMap[r0][c0] = 1

        while pointList:
            pointTempList = []
            for point in pointList:
                for i in range(len(value1)):
                    x = point[0] + value1[i]
                    y = point[1] + value2[i]
                    if 0 <= x < R and 0 <= y < C and 0 == valueMap[x][y]:
                        valueMap[x][y] = 1
                        temp = [x, y]
                        pointTempList.append(temp)
                        result.append(temp)

            pointList = pointTempList

        return result

