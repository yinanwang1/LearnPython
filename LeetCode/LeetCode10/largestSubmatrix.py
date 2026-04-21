from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row, column =len(matrix), len(matrix[0])
        for i in range(1, row):
            for j in range(column):
                if 1 == matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

        answer = 0
        for i in range(row):
            matrix[i].sort(reverse=True)
            for j in range(column):
                answer = max(answer, matrix[i][j] * (j + 1))

        return answer


if __name__ == '__main__':
    # matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]
    # matrix = [[1,0,1,0,1]]
    matrix = [[0,0],[0,0]]
    # matrix = [[1,1,0],[1,0,1]]
    solution = Solution()
    res = solution.largestSubmatrix(matrix)
    print(res)