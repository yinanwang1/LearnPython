from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        ans = [[0 for _ in range(col - k + 1)] for _ in range(row - k + 1)]
        if 1 >= k:
            return ans
        for i in range(row):
            if i + k > row:
                break
            for j in range(col):
                if j + k > col:
                    break
                elements = set()
                for s in range(i, i + k):
                    for t in range(j, j + k):
                        elements.add(grid[s][t])
                values = sorted(list(elements))
                if 1 == len(values):
                    ans[i][j] = 0
                else:
                    abs_values = []
                    for v in range(len(values) - 1):
                        abs_values.append(abs(values[v] - values[v + 1]))
                    ans[i][j] = min(abs_values)

        return ans


if __name__ == '__main__':
    solution = Solution()
    # grid = [[1,8],[3,-2]]
    # k = 2
    grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    k = 5
    ans = solution.minAbsDiff(grid, k)
    print(ans)
