



from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m, MOD = len(grid), len(grid[0]), 12345
        p = [[ 1 for _ in range(m)] for _ in range(n)]

        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suffix
                suffix = (grid[i][j] * suffix) % MOD

        prefix = 1
        for i in range(n):
            for j in range(m):
                value = grid[i][j]
                grid[i][j] = (prefix * p[i][j]) % MOD
                prefix = (prefix * value) % MOD

        return grid


if __name__ == '__main__':
    sol = Solution()
    # grid = [[12345],[2],[1]]
    grid = [[1,2],[3,4]]
    print(sol.constructProductMatrix(grid))