# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
#
# 函数 myAtoi(string s) 的算法如下：
#
# 读入字符串并丢弃无用的前导空格
# 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
# 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
# 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
# 如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
# 返回整数作为最终结果。
# 注意：
#
# 本题中的空白字符只包括空格字符 ' ' 。
# 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。


class Solution:
    def myAtoi(self, s: str) -> int:
        if 0 == len(s):
            return 0

        minus = False
        value = list()
        find = False
        index = 0

        while index < len(s):
            v = s[index]
            index += 1
            if find:
                if 0x30 == ord(v):
                    if 0 != len(value):
                        value.append(v)
                elif 0x30 < ord(v) <= 0x39:
                    value.append(v)
                else:
                    if len(value) == 0:
                        return 0
                    break
            else:
                if v == ' ':
                    continue
                elif v == '+':
                    find = True
                    minus = False
                elif v == '-':
                    find = True
                    minus = True
                elif 0x30 <= ord(v) <= 0x39:
                    find = True
                    minus = False
                    if 0x30 != ord(v):
                        value.append(v)
                else:
                    return 0

        if 0 == len(value):
            return 0

        maxV = 2**31
        maxS = str(maxV)
        maxL = len(maxS)
        valueS = "".join(value)
        if len(value) > maxL:
            return -maxV if minus else maxV - 1
        elif len(value) < maxL:
            return -int(valueS) if minus else int(valueS)
        else:
            for i in range(maxL):
                if value[i] > maxS[i]:
                    return -maxV if minus else maxV - 1
                elif value[i] < maxS[i]:
                    return -int(valueS) if minus else int(valueS)

            return -int(valueS) if minus else int(valueS) - 1







