class Solution:
    def romanToInt(self, s: str) -> int:
        romanDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        romainSpecial = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        result = 0
        index = 0

        while index < len(s):
            temp = s[index: index + 2]
            if temp in romainSpecial.keys():
                result += romainSpecial[temp]
                index += 2
                continue

            temp = s[index: index + 1]
            result += romanDic[temp]
            index += 1

        return result
