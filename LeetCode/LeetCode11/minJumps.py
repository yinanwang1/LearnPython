from collections import defaultdict
from typing import List

# 3629. 通过质数传送到达终点的最少跳跃次数
# https://leetcode.cn/problems/minimum-jumps-to-reach-end-via-prime-teleportation/description/


max_value = 10 ** 6 + 1
factors = [[] for _ in range(max_value)]
for i in range(2, max_value):
    if not factors[i]:
        for j in range(i, max_value, i):
            factors[j].append(i)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        num_positions = defaultdict(list)
        for i, num in enumerate(nums):
            if 1 == len(factors[num]):
                num_positions[num].append(i)

        n = len(nums)
        visited = [False] * n
        visited[n - 1] = True
        q = [n - 1]
        res = 0
        while True:
            q2 = []
            for i in q:
                if 0 == i:
                    return res
                if i > 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q2.append(i - 1)
                if i < n - 1 and not visited[i + 1]:
                    visited[i + 1] = True
                    q2.append(i + 1)
                for num in factors[nums[i]]:
                    for j in num_positions[num]:
                        if not visited[j]:
                            visited[j] = True
                            q2.append(j)
                    num_positions[nums[i]].clear()
            res += 1
            q = q2


if __name__ == '__main__':
    print(Solution().minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
