from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix) - 1
        for i in range(N):
            for j in range(i, N - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[N - j][i]
                matrix[N - j][i] = matrix[N - i][N - j]
                matrix[N - i][N - j] = matrix[j][N - i]
                matrix[j][N - i] = temp


solution = Solution()
solution.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])
print('END')