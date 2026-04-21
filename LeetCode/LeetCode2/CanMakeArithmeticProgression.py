from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        num = arr[1] - arr[0]

        for index in range(1, len(arr)):
            if num != arr[index] - arr[index - 1]:
                return False

        return True
