

# 判断子序列
# https://leetcode.cn/problems/is-subsequence/description/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]
        add = 0
        for i in range(n):
            v = f[add][ord(s[i]) - ord('a')]
            if v == m:
                return False
            add = v + 1

        return True
