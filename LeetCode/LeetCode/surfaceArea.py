from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total_area = 0
        N = len(grid)

        for row in range(N):
            for column in range(N):
                value = grid[row][column]

                if 0 == value:
                    continue

                total_area += 2

                if column - 1 >= 0:
                    if grid[row][column - 1] < value:
                        total_area += value - grid[row][column - 1]
                else:
                    total_area += value

                if column + 1 < N:
                    if grid[row][column + 1] < value:
                        total_area += value - grid[row][column + 1]
                else:
                    total_area += value

                if row - 1 >= 0:
                    if grid[row - 1][column] < value:
                        total_area += value - grid[row - 1][column]
                else:
                    total_area += value

                if row + 1 < N:
                    if grid[row + 1][column] < value:
                        total_area += value - grid[row + 1][column]
                else:
                    total_area += value

        return total_area


solution = Solution()
result = solution.surfaceArea([[1,1,1],[1,0,1],[1,1,1]])
print('END')
print(result)