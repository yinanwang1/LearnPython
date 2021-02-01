from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        result = 0
        for value in boxTypes:
            nums = value[0] if truckSize >= value[0] else truckSize
            result += nums * value[1]
            truckSize -= nums

            if truckSize == 0:
                break
        return result
