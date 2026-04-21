# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        odd = l % 2 == 0
        v = l // 2 if odd else (l - 1) // 2
        y = l // 2 if odd else (l + 1) // 2
        print(v)
        print(y)
        for i in range(v):
            for j in range(y):
                n = l - i - 1
                m = l - j - 1
                t = matrix[i][j]
                matrix[i][j] = matrix[m][i]
                matrix[m][i] = matrix[n][m]
                matrix[n][m] = matrix[j][n]
                matrix[j][n] = t
