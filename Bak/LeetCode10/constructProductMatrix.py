



from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        if 0 == n and 0 == m:
            grid[0][0] = 0
            return grid

        temp = [[[1] * 2 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # 计算之前的所有数乘积
                s, t = i, j - 1
                if t < 0:
                    s -= 1
                    if s >= 0:
                        t = m - 1
                    else:
                        s = t = 0
                temp[i][j][0] = (grid[i][j] * temp[s][t][0]) % 12345

                # 计算之后的所有数乘积
                f, b = n - 1 - i, m - 1 - j
                x, y = f, b + 1
                if y >= m:
                    x += 1
                    if x < n:
                        y = 0
                    else:
                        x, y = n - 1, m -1
                temp[f][b][1] = (grid[f][b] * temp[x][y][1]) % 12345

        for i in range(n):
            for j in range(m):
                s, t = i, j - 1
                if t < 0:
                    s -= 1
                    if s >= 0:
                        t = m - 1
                    else:
                        s = t = 0
                x, y = i, j + 1
                if y >= m:
                    x += 1
                    if x < n:
                        y = 0
                    else:
                        x, y = n - 1, m -1
                if 0 == i and 0 == j:
                    grid[i][j] = temp[x][y][1]
                    continue
                elif n - 1 == i and m -1 == j:
                    grid[i][j] = temp[s][t][0]
                    continue
                else:
                    grid[i][j] = (temp[s][t][0] * temp[x][y][1]) % 12345

        return grid


if __name__ == '__main__':
    sol = Solution()
    # grid = [[12345],[2],[1]]
    grid = [[1,2],[3,4]]
    print(sol.constructProductMatrix(grid))