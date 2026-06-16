



# 3612. 用特殊操作处理字符串 I
# https://leetcode.cn/problems/process-string-with-special-operations-i/description/



class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for char in s:
            if char == '*':
                if result:
                    result.pop()
            elif char == '#':
                result += result
            elif char == '%':
                result.reverse()
            else:
                result.append(char)

        return "".join(result)

