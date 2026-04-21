class Solution:
    def hammingWeight(self, n: int) -> int:
        binStr = bin(n)
        return binStr.count('1')