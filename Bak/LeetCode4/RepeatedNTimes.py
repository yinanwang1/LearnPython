from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        from collections import Counter
        counter = dict(Counter(A))
        times = len(counter.keys())
        for k, v in counter.items():
            if v == times:
                return k