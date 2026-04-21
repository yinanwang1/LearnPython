from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        sum = 0
        for (_, value) in dict(c).items():
            if value > 1:
                sum += (value * (value + 1) / 2)

        return sum