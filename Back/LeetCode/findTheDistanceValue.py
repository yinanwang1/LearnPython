from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        number = 0

        for item in arr1:
            success = True
            for cell in arr2:
                if abs(item - cell) <= d:
                    success = False
                    break

            if success:
                number += 1

        return number



