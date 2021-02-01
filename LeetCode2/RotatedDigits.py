class Solution:
    def rotatedDigits(self, N: int) -> int:
        result = 0
        for v in range(2, N):
            if '3' in str(v) or '4' in str(v) or '7' in str(v):
                continue

            if '2' in str(v) or '5' in str(v) or '6' in str(v) or '9' in str(v):
                result += 1

        return result
