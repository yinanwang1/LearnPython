from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 如果起点和终点是小偷，那么安全距离就是0了。
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        # 记录每一个点的安全距离，如果是小偷，那么安全距离为0
        dis = [[-1] * n for _ in range(n)]
        # 每一个点的上下左右
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque()

        # 找到每一个小偷，设置小偷的安全距离为0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dis[i][j] = 0

        # 记录每一个点的安全距离。 使用了一个队列，方便出队。
        # 先按小偷的队列进行遍历，然后将小偷四周的点入队
        # 如果点已经计算过则跳过
        while q:
            cx, cy = q.popleft()
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and dis[nx][ny] == -1:
                    dis[nx][ny] = dis[cx][cy] + 1
                    q.append((nx, ny))

        # 从（0，0）到（n-1， n-1）判断是否都大于等于limit
        # 如果不是，则返回False，如果通过到达（n-1,n-1）则返回True
        def check(limit: int) -> bool:
            visit = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            visit[0][0] = True

            while q:
                cx, cy = q.popleft()
                if cx == n - 1 and cy == n - 1:
                    return True
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and dis[nx][ny] >= limit:
                        q.append((nx, ny))
                        visit[nx][ny] = True
            return False

        # 起点和终点是安全距离的天花板
        lo, hi = 0, min(dis[0][0], dis[n - 1][n - 1])
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            # 如果满足了，那么再试试更大的值
            if check(mid):
                res = mid
                lo = mid + 1
            else:
                # 如果不满足了，那么就再试试更小的值
                hi = mid - 1

        return res
