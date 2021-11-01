from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        values = list()
        lastValue = -1
        times = 1

        for index in range(0, len(arr) + 1, int(len(arr) / 8 - 1)):
            if arr[index] == lastValue:
                values.append(lastValue)
                times += 1
                if times == 3:
                    return lastValue
                continue

            lastValue = arr[index]
            times = 1

        if 1 == len(values):
            return values[0]

        for value in values:
            index = arr.index(value)
            if value == arr[index + int(len(arr) / 4)]:
                return value

        return arr[0]

