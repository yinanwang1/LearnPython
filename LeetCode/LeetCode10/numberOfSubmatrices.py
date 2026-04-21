from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0
        s = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                s[i + 1][j + 1][0] = s[i][j + 1][0] + s[i + 1][j][0] - s[i][j][0]
                s[i + 1][j + 1][1] = s[i][j + 1][1] + s[i + 1][j][1] - s[i][j][1]
                if "." != col:
                    s[i + 1][j + 1][ord(col) & 1] += 1
                if s[i + 1][j + 1][0] == s[i + 1][j + 1][1] > 0:
                    res += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    # grid = [["X", "Y", "."], ["Y", ".", "."]]
    grid = [[".", ".", "."], [".", "X", "X"], ["Y", ".", "."], ["X", ".", "."]]
    print(sol.numberOfSubmatrices(grid))
