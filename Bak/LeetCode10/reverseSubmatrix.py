from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        half = k // 2
        times = k - 1
        for i in range(x, x+half):
            for j in range(y, y+k):
                grid[i][j], grid[i + times][j] = grid[i + times][j], grid[i][j]
            times -= 2

        return grid
