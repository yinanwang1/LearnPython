class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            num = columnNumber % 26
            if num == 0:
                result = 'Z' + result
                columnNumber -= 26
            else:
                result = chr(num + 64) + result

            columnNumber //= 26

        return result