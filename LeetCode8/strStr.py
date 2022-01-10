# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def calc(self, needle: str) -> list:
        next = [-1] * len(needle)
        k = -1
        j = 0
        while j < len(needle) - 1:
            if -1 == k or needle[k] == needle[j]:
                j += 1
                k += 1
                next[j] = k
            else:
                k = next[k]

        return next

    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None or 0 == len(needle):
            return 0
        next = self.calc(needle)
        i = 0
        j = 0

        while i < len(haystack) and j < len(needle):
            if -1 == j or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]

        if j == len(needle):
            return i - j

        return -1
