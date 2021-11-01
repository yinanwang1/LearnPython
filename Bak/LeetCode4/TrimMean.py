from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        length = int(len(arr) * 0.05)
        valueList = arr[length:-length]
        return sum(valueList) / len(valueList)