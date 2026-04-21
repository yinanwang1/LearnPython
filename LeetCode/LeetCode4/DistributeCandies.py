from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        from collections import Counter
        nums = len(dict(Counter(candyType)).keys())
        return nums if nums <= len(candyType)//2 else len(candyType)//2
