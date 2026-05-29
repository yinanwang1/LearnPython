from typing import List



# Q1. 判断能否形成等差数列
# https://leetcode.cn/problems/can-make-arithmetic-progression-from-sequence/description/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        value = arr[1] - arr[0]
        for index in range(2, len(arr)):
            if arr[index] - arr[index - 1] != value:
                return False
        else:
            return True



