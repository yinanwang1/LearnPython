from collections import Counter


# 1189. “气球” 的最大数量
# https://leetcode.cn/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter([ch for ch in text if ch in "balon"])
        cnt['l'] //= 2
        cnt['o'] //= 2

        return min(cnt.values()) if len(cnt) == 5 else 0