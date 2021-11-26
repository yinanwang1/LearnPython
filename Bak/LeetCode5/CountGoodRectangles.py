from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxValue = 0
        times = 0

        for x, y in rectangles:
            value = min(x, y)
            if value > maxValue:
                times = 1
                maxValue = value
            elif value == maxValue:
                times += 1

        return times