class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bCount = aCount = lCount = oCount = nCount = 0
        for char in text:
            if char == 'b':
                bCount += 1
            elif char == 'a':
                aCount += 1
            elif char == 'l':
                lCount += 1
            elif char == 'o':
                oCount += 1
            elif char == 'n':
                nCount += 1

        return min(aCount, bCount, lCount // 2, oCount // 2, nCount)
