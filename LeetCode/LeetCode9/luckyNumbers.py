
# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.


from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        columnMax = [-1 for _ in range(len(matrix[0]))]
        for columnIndex, row in enumerate(matrix):
            minValue, index = 10000000, 0
            for i, v in enumerate(row):
                if v < minValue:
                    minValue = v
                    index = i

            if -1 != columnMax[index]:
                if columnIndex == columnMax[index]:
                    result.append(minValue)
            else:
                maxValue, maxIndex = 0, 0
                for i in range(len(matrix)):
                    v = matrix[i][index]
                    if v > maxValue:
                        maxValue = v
                        maxIndex = i
                columnMax[index] = maxIndex
                if maxIndex == columnIndex:
                    result.append(maxValue)

        return result




