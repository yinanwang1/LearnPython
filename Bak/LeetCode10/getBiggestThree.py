from typing import List

# https://leetcode.cn/problems/get-biggest-three-rhombus-sums-in-a-grid/description/?envType=daily-question&envId=2026-03-16&status=NOT_STARTED&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJBQ19SQVRFIn1d&difficulty=EASY

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        border = min(m, n)
        res = set([x for row in grid for x in row])
        for x in range(m):
            for y in range(n):
                for k in range(1, border + 1):
                    if y + 2 * k >= n or x + k >= m or x -k < 0:
                        continue
                    total = 0
                    r = x
                    c = y
                    for l in range(1, k + 1):
                        r -= 1
                        c += 1
                        total += grid[r][c]

                    for l in range(1, k + 1):
                        r += 1
                        c += 1
                        # print("second r is {}, c is {}".format(str(r), str(c)))
                        total += grid[r][c]

                    for l in range(1, k + 1):
                        r += 1
                        c -= 1
                        total += grid[r][c]

                    for l in range(1, k + 1):
                        r -= 1
                        c -= 1
                        total += grid[r][c]

                    res.add(total)
                    # print(total)

        res = sorted(res, reverse=True)

        print(res)

        return list(res)[0:3]














