from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        nums = 0
        for num in arr:
            if num % 2 == 1:
                num += 1
                if num >= 3:
                    return True
            else:
                num = 0

        return False
