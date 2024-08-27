# 给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。



from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)
        high = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                high = i
            bits[i] = bits[i - high] + 1

        return bits
