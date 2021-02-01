from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        from collections import Counter
        valueDict = dict(Counter(arr1))
        result = list()
        for value in arr2:
            result.extend([value] * valueDict[value])
            del valueDict[value]
        for key,value in valueDict.items():
            result.extend([key] * value)

        return result