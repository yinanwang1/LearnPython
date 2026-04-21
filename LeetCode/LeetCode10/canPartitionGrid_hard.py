from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = 0
        grid_temp = grid
        for i in range(m):
            for j in range(n):
                total += grid_temp[i][j]

        for _ in range(4):
            m, n = len(grid_temp), len(grid_temp[0])
            if m < 2:
                grid_temp = self.rotate(grid_temp)
                continue
            sum_value = 0
            existed = {0}
            if 1 == n:
                for i in range(m-1):
                    sum_value += grid_temp[i][0]
                    tag = 2 * sum_value - total
                    if 0 == tag or grid_temp[0][0] == tag or grid_temp[i][0] == tag:
                        return True
                grid_temp = self.rotate(grid_temp)
                continue
            for i in range(m - 1):
                for j in range(n):
                    sum_value += grid_temp[i][j]
                    existed.add(grid_temp[i][j])
                tag = 2 * sum_value - total
                if 0 == i:
                    if 0 == tag or grid_temp[0][0] == tag or grid_temp[0][n - 1] == tag:
                        return True
                    continue
                if tag in existed:
                    return True
            grid_temp = self.rotate(grid_temp)

        return False

    def rotate(self, grid_temp: List[List[int]]) -> List[List[int]]:
        m, n = len(grid_temp), len(grid_temp[0])
        temp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                temp[j][m - i - 1] = grid_temp[i][j]

        return temp


if __name__ == '__main__':
    # grid = [[10, 5, 4, 5]]
    # grid = [[1, 2, 4], [2, 3, 5]]
    grid = [[5,5,6,2,2,2]]
    print(Solution().canPartitionGrid(grid))
