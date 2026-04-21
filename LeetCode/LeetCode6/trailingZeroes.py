class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 1
        for i in range(1, n + 1):
            num *= i

        result = 0
        while True:
            n = num % 10
            if 0 == n:
                result += 1
                num //= 10
            else:
                break

        return result

