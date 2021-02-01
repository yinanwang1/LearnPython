from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        if S is None or 0 == len(S):
            return list()

        path = ''
        result = list()

        def recursion(s, p, r):
            if 0 == len(s):
                r.append(p)
                return

            for i in range(len(s)):
                char = s[i]
                recursion(s[:i] + s[i+1:], p + char, r)

        recursion(S, path, result)

        return result






