class Solution:
    def binaryGap(self, n: int) -> int:
        if 0 == n:
            return 0
        binary = str(bin(n))
        maxLength = 0
        index = binary.find('1')
        for i in range(index + 1, len(binary)):
            if binary[i] == '1':
                maxLength = max(maxLength, i - index)
                index = i

        return maxLength