# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()
        i = 0
        for c in s:
            if c in d.keys():
                k, v = d[c]
                d[c] = i, v + 1
            else:
                d[c] = i, 1
            i += 1

        for k, v in d.values():
            if v == 1:
                return k

        return -1

