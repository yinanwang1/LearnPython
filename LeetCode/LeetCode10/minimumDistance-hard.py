from functools import cache
from itertools import pairwise

# 预处理两个字母的距离
COLUMN = 6
get_dis = lambda a, b: abs(a // COLUMN - b // COLUMN) + abs(a % COLUMN - b % COLUMN)
dis = [[get_dis(i, j) for j in range(26)] for i in range(26)]


class Solution:
    def minimumDistance(self, word: str) -> int:
        word = [ord(c) - ord('A') for c in word]
        n = len(word)
        @cache
        def dfs(i: int, finger1: int, finger2: int) -> int:
            if i < 0:
                return 0
            res1 = dfs(i - 1, finger1, word[i]) + dis[finger2][word[i]]
            res2 = dfs(i -1, word[i], finger2) + dis[finger1][word[i]]

            return min(res1, res2)

        return min([dfs(n-2, word[-1], finger) for finger in range(26)])


if __name__ == '__main__':
    print(Solution().minimumDistance("CAKE"))
    # print(Solution().minimumDistance("HAPPY"))
    # print(Solution().minimumDistance("JDX"))
