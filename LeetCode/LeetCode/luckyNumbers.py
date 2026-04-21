from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = list()
        rows = len(matrix)

        for index in range(rows):
            row_list = matrix[index]
            min_num = min(row_list)
            min_index = row_list.index(min_num)

            column_list = list()
            for i in range(rows):
                column_list.append(matrix[i][min_index])

            if min_num == max(column_list):
                result.append(min_num)

        return result
