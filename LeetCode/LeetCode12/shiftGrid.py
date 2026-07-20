from typing import List


# 二维网格迁移
# https://leetcode.cn/problems/shift-2d-grid/description/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        simple_k = k % (m * n)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                v = (n * i + j - simple_k + m * n) % (m * n)
                next_i = (v // n) % m
                next_j = v % n
                res[i][j] = grid[next_i][next_j]

        return res


if __name__ == '__main__':
    grid = [[1],[2],[3],[4],[7],[6],[5]]
    k = 23
    print(Solution().shiftGrid(grid, k))
