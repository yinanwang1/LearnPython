# 实现 strStr() 函数。
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。
# 说明：
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None or 0 == len(needle):
            return 0

        if haystack is None or 0 == len(haystack):
            return -1

        f = needle[0]
        hl = len(haystack)
        l = len(needle)
        for i, v in enumerate(haystack):
            if hl - i < l:
                return -1
            if f == v and haystack[i: i + l] == needle:
                return i

        return -1