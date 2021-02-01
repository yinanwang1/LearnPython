from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        result = 0

        for i in range(0, length - 2):
            first = arr[i]
            for j in range(i + 1, length - 1):
                second = arr[j]
                for k in range(j + 1, length):
                    third = arr[k]
                    if abs(first - second) <= a \
                        and abs(second - third) <= b \
                        and abs(first - third) <= c:
                            result += 1

        return result

