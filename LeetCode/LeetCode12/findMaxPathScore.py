import heapq
from typing import List


# 3620. 恢复网络路径
# https://leetcode.cn/problems/network-recovery-pathways/


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            l = min(l, w)
            r = max(r, w)

        def check(mid: int) -> bool:
            dis = [float("inf")] * n
            pq = [(0, 0)]
            dis[0] = 0

            while pq:
                d, u = heapq.heappop(pq)

                if d > k:
                    return False
                if u == n - 1:
                    return True
                if d > dis[u]:
                    continue

                for v, w in g[u]:
                    if w < mid:
                        continue
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(pq, (dis[v], v))
            return False

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r




if __name__ == '__main__':
    s = Solution()
    # print(s.findMaxPathScore([[0,1,5],[1,3,10],[0,2,3],[2,3,4]], [True,True,True,True], 10))
    print(s.findMaxPathScore([[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], [True,True,True,False,True], 12))