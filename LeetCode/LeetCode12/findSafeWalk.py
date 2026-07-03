import heapq
from typing import List


# 3286. 穿越网格图的安全路径
# https://leetcode.cn/problems/find-a-safe-walk-through-a-grid/description/

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dis = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        pq = [(grid[0][0], 0, 0)]
        while pq:
            # 小顶堆，弹出是cost最小的。
            val, cx, cy = heapq.heappop(pq)
            if dis[cx][cy] >= 0:
                continue
            dis[cx][cy] = val
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and dis[nx][ny] == -1:
                    heapq.heappush(pq, (val + grid[nx][ny], nx, ny))

        return dis[m - 1][n - 1] < health


if __name__ == '__main__':
    grid = [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]]
    health = 3

    s = Solution()
    print(s.findSafeWalk(grid, health))
