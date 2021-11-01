from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxValue = 0
        altitude = 0
        for value in gain:
            altitude += value
            maxValue = max(maxValue, altitude)

        return maxValue