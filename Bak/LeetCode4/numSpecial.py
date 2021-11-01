from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        columns = []
        for nums in mat:
            if 1 == sum(nums):
                columns.append(nums.index(1))

        result = 0
        for column in columns:
            sumColumn = 0
            for i in range(len(mat)):
                sumColumn += mat[i][column]

            if 1== sumColumn:
                result += 1

        return result

