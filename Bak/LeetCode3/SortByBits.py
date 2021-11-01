from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        sortedDic = dict()
        for num in arr:
            numBin = str(bin(num)).count('1')
            nums = sortedDic.get(numBin, list())
            nums.append(num)
            nums.sort()
            sortedDic.setdefault(numBin, nums)

        keysList = list(sortedDic.keys())
        keysList.sort()

        result = list()
        for key in keysList:
            result += sortedDic.get(key)

        return result
