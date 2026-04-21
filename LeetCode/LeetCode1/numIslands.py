from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) <= 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        def isIsland(row: int, column: int):
            if grid[row][column] != '1':
                return

            grid[row][column] = '2'

            for x, y in [(row, column - 1), (row + 1, column), (row, column + 1), (row - 1, column)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == '1':
                        isIsland(x, y)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    isIsland(i, j)

        return count

