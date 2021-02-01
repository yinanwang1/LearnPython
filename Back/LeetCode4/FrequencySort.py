from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        from functools import reduce
        nums.sort(reverse=True)
        counts = dict(Counter(nums))
        tupleList = list(counts.items())
        sortedTupleList = sorted(tupleList, key=lambda d: d[1])
        temp = list(map(lambda d: [d[0]] * d[1], sortedTupleList))

        return reduce(lambda x,y: x + y, temp)

