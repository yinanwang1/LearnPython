from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if mat == target:
            return True
        for _ in range(3):
            for i in range( n // 2):
                for j in range(i, n - i - 1):
                    mat[i][j], mat[n - 1 - j][i], mat[n-1-i][n-1-j], mat[j][n-1-i] =\
                        mat[n - 1 - j][i], mat[n-1-i][n-1-j], mat[j][n-1-i], mat[i][j]
            if mat == target:
                return True

        return False



if __name__ == '__main__':
    # target = [[1, 0], [0, 1]]
    target = [[1,1,1],[0,1,0],[0,0,0]]
    # mat = [[0,1],[1,0]]
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    res = solution.findRotation(mat, target)