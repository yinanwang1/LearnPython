class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binNum = str(bin(n))
        for i in range(1, len(binNum)):
            if binNum[i] == binNum[0]:
                return False

        return True