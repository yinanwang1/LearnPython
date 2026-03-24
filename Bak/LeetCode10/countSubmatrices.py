from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(1, col):
                grid[i][j] += grid[i][j - 1]

            if i > 0:
                for j in range(col):
                    grid[i][j] += grid[i - 1][j]

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] <= k:
                    res += 1
                else:
                    break

        return res
