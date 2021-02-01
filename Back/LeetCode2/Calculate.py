class Solution:
    def calculate(self, s: str) -> int:
        x = 1
        y = 0
        for char in s:
            if 'A' == char:
                x = 2 * x + y
            else:
                y = 2 * y + x

        return x + y
        