from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        row = len(grid)
        column = len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    for k in range(4):
                        iTemp = i + dx[k]
                        jTemp = j + dy[k]
                        if iTemp < 0 or iTemp >= row or jTemp < 0 or jTemp >= column or 0 == grid[iTemp][jTemp]:
                            perimeter += 1

                print("i is {0}, j is {1}, perimeter is {2}".format(i, j, perimeter))

        return perimeter


