# 给定一个正整数 n ，输出外观数列的第 n 项。
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
# 你可以将其视作是由递归公式定义的数字字符串序列：
# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            result = self.calcNumber(result)

        return result

    def calcNumber(self, pre_str: str) -> str:
        result = ""
        num = 0
        v = ""
        for c in pre_str:
            if num == 0:
                num = 1
                v = c
            else:
                if c == v:
                    num += 1
                else:
                    result += str(num) + v
                    num = 1
                    v = c
        if num != 0:
            result += str(num) + v

        return result


