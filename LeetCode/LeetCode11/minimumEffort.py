from typing import List


# 1665. 完成所有任务的最少初始能量
# https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        total_energy = sum(map(lambda x: x[0], tasks))
        base_energy = total_energy
        for a, m in tasks:
            if base_energy < m:
                total_energy += m - base_energy
                base_energy = m
            base_energy -= a

        return total_energy


if __name__ == '__main__':
    print(Solution().minimumEffort(tasks=[[1,2],[2,4],[4,8]]))