

# 3614. 用特殊操作处理字符串 II
# https://leetcode.cn/problems/process-string-with-special-operations-ii/



class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        for c in s:
            if c == '*':
                if length:
                    length -=  1
            elif c == "#":
                length *= 2
            elif c == "%":
                continue
            else:
                length += 1
        if k >= length:
            return "."

        for c in reversed(s):
            if c == "*":
                length += 1
            elif c == "#":
                length //= 2
                if k >= length:
                    k -= length
            elif c == "%":
                k = length - k - 1
            else:
                if k == length - 1:
                    return c
                length -= 1

        return "."




