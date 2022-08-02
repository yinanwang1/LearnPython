from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        pairs = 0
        left = 0
        for k, v in counter.items():
            pairs += v // 2
            left += v % 2

        return [pairs, left]



