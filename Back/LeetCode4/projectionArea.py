from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0
        n = len(grid)
        for row in grid:
            area += max(row)
            area += n - row.count(0)

        gridChange = list(zip(*grid))
        for row in gridChange:
            area += max(row)

        return area
