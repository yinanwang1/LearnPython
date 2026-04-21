class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last, cur, res = 0, 1, 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                last = cur
                cur = 1

            if last >= cur:
                res += 1

        return res


