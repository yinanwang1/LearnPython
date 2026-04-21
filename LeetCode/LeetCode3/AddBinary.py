class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = bin(int('0b' + a, 2) + int('0b' + b, 2))
        return result.replace('0b', '')
