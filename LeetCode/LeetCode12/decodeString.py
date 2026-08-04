

# 394. 字符串解码
# https://leetcode.cn/problems/decode-string/




class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for char in s:
            if char == "[":
                stack.append([res, multi])
                res, multi = "", 0
            elif char == "]":
                last_res, last_multi = stack.pop()
                res = last_res + last_multi * res
            elif "0" <= char <= "9":
                multi = 10 * multi + int(char)
            else:
                res += char
        return res


if __name__ == '__main__':
    solution = Solution()
    # print(solution.decodeString("3[a]2[bc]"))
    print(solution.decodeString("3[a2[c]]"))