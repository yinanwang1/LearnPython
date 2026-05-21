from typing import List



# 3043. 最长公共前缀的长度
# https://leetcode.cn/problems/find-the-length-of-the-longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen = set()
        for num in arr1:
            while num:
                seen.add(num)
                num //= 10
        ans = 0
        for num in arr2:
            while num:
                if num in seen:
                    ans = max(num, ans)
                    break
                num //= 10

        return 0 if 0 == ans else len(str(ans))



