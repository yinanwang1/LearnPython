from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or 0 >= len(strs):
            return ""

        for i in range(0, len(strs[0])):
            char = strs[0][i]
            for j in range(0, len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return strs[0][0: i]

        return strs[0]
