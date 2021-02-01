from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = list()
        minus = abs(arr[1] - arr[0])
        arr.sort()

        for index in range(1, len(arr)):
            minusTemp = abs(arr[index] - arr[index - 1])
            pair = [arr[index - 1], arr[index]]
            if minusTemp < minus:
                result.clear()
                result.append(pair)
                minus = minusTemp
            elif minusTemp == minus:
                result.append(pair)

        return result
                