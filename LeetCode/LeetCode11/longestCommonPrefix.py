from typing import List



# 3043. 最长公共前缀的长度
# https://leetcode.cn/problems/find-the-length-of-the-longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes:dict[str, int] = {}
        for i in range(len(arr1)):
            value = str(arr1[i])
            for l in range(len(value)):
                prefixes.setdefault(value[:l + 1], 1)
        ans = 0
        for j in arr2:
            value = str(j)
            if ans >= len(value):
                continue
            for index in range(len(value), -1, -1):
                if ans >= index +1:
                    break
                v = prefixes.get(value[:index], 0)
                if v:
                    ans = max(index, ans)
                    break

        return ans


