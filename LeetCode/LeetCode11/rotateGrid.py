from typing import List


# 1914. 循环轮转矩阵
# https://leetcode.cn/problems/cyclically-rotating-a-grid/description/


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        start_row, start_col, end_row, end_col = 0, 0, m - 1, n - 1

        while start_row <= end_row and start_col <= end_col:
            temps = []
            positions = []
            for i in range(start_col, end_col):
                positions.append((start_row, i))
                temps.append(grid[start_row][i])
            for i in range(start_row, end_row):
                positions.append((i, end_col))
                temps.append(grid[i][end_col])
            for i in range(end_col, start_col, -1):
                positions.append((end_row, i))
                temps.append(grid[end_row][i])
            for i in range(end_row, start_row, -1):
                positions.append((i, start_col))
                temps.append(grid[i][start_col])
            times = k % len(temps)
            for i ,(x, y) in enumerate(positions):
                index = (i + times + len(temps)) % len(temps)
                grid[x][y] = temps[index]
            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1

        return grid


if __name__ == '__main__':
    print(Solution().rotateGrid(grid=[[40,10],[30,20]], k=1))