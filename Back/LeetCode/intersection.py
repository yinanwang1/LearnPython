from typing import List

class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        def function(start: List[int], end: List[int]) -> (int, int):
            k = (start[1] - end[1]) / (start[0] - end[0])
            l = end[1] - k * end[0]

            return k, l

        if start1[0] == end1[0]:
            if start2[0] == end2[0]:
                if start1[0] == start2[0]:
                    if end2[1] > start2[1]:
                        max_value = end2[1]
                        min_value = start2[1]
                    else:
                        max_value = start2[1]
                        min_value = end2[1]
                    if min_value <= start1[1] <= max_value:
                        return [start1[0], start1[1]]
                    elif min_value <= end1[1] <= max_value:
                        return [start1[0], max(start1[1], start2[1])]
                    else:
                        return []
                else:
                    return []
            else:
                k, l = function(start2, end2)
                y = k * start1[0] + l
                if start1[1] <= y <= end1[1]:
                    return [start1[0], y]
                else:
                    return []
        else:
            if start2[0] == end2[0]:
                k, l = function(start1, end1)
                y = k * start2[0] + l
                if start2[1] <= y <= end2[1]:
                    return [start2[0], y]
                else:
                    return []

        x_left = max(start1[0], start2[0])
        x_right = min(end1[0], end2[0])
        k1, l1 = function(start1, end1)
        k2, l2 = function(start2, end2)

        if k1 == k2 and l1 == l2:
            y = k1 * x_left + l1

            return [x_left, y]

        left, right = x_left, x_right
        result = False
        while left < right:
            mid = float(left + right) / 2.0
            y1 = mid * k1 + l1
            y2 = mid * k2 + l2

            if -0.000001 < y1 - y2 < 0.000001:
                left = mid
                right = min(y1, y2)
                result = True
                break

            if k1 > k2:
                if y1 > y2:
                    right = mid
                else:
                    left = mid
            else:
                if y1 > y2:
                    left = mid
                else:
                    right = mid

        if result:
            return [left, right]
        else:
            return []










