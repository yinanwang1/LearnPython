from typing import List
from functools import reduce


def add(x, y):
    return x + y


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for length in range(1, len(arr) + 1, 2):
            result += self.sumSubArray(arr, length)

        return result

    def sumSubArray(self, arr: List[int], length: int) -> int:
        resultSum = 0
        for i in range(0, len(arr) - length + 1):
            tempArr = arr[i: i + length]
            resultSum += reduce(add, tempArr)

        return resultSum




solution = Solution()
result = solution.sumOddLengthSubarrays([1,4,2,5,3])
print("***************")
print("END is " + str(result))