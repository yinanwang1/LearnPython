# 1137. 第 N 个泰波那契数
# https://leetcode.cn/problems/n-th-tribonacci-number/description/?envType=problem-list-v2&envId=dynamic-programming


class Solution:
    def tribonacci(self, n: int) -> int:
        def dfs(index: int) -> int:
            if 0 == index:
                return 0
            if 1 == index:
                return 1
            if 2 == index:
                return 1
            return dfs(index - 1) + dfs(index - 2) + dfs(index - 3)

        return dfs(n)
