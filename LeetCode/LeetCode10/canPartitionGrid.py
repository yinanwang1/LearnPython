from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = 0
        temp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                temp[i + 1][j + 1] = temp[i + 1][j] + temp[i][j + 1] - temp[i][j] + grid[i][j]
                total += grid[i][j]
        for i in range(1, m):
            if total == 2 * temp[i][n]:
                return True
        for j in range(1, n):
            if total == 2 * temp[m][j]:
                return True

        return False


if __name__ == '__main__':
    # grid = [[1, 4], [2, 3]]
    grid = [[100000,100000,92687]]
    solution = Solution()
    print(solution.canPartitionGrid(grid))
