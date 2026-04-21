class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        total = 0
        for value in str(num):
            total += int(value)

        return self.addDigits(total)