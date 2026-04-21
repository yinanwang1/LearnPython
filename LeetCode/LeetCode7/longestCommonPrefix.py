# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        index = 0
        while True:
            c = None
            for s in strs:
                if index >= len(s):
                    return result
                if c is None:
                    c = s[index]
                else:
                    if c == s[index]:
                        continue
                    else:
                        return result

            result += c
            index += 1
