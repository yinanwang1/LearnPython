# Given a list of 24-hour clock time points in "HH:MM" format,
# return the minimum minutes difference between any two time-points in the list.


from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutesList = []
        for time in timePoints:
            l = time.split(':')
            minutesList.append(int(l[0]) * 60 + int(l[1]))
        minutesList.sort()
        minValue = minutesList[1] - minutesList[0]
        for i in range(1, len(minutesList) - 1):
            minValue = min(minValue, minutesList[i + 1] - minutesList[i])
        minValue = min(minValue, 60 * 24 - minutesList[-1] + minutesList[0])

        return minValue
