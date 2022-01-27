
# You are given a stream of points on the X-Y plane. Design an algorithm that:
# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated
# as different points.
# Given a query point, counts the number of ways to choose three points from the data structure
# such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel
# or perpendicular to the x-axis and y-axis.
#
# Implement the DetectSquares class:
#
# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y]
# as described above.

from typing import List
from collections import defaultdict, Counter


class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if point[0] in self.points.keys():
            value = self.points.get(point[0])
            if point[1] in value.keys():
                value[point[1]] = value.get(point[1]) + 1
            else:
                value[point[1]] = 1
        else:
            self.points.setdefault(point[0], {point[1]: 1})

    def count(self, point: List[int]) -> int:
        if point[0] not in self.points.keys():
            return 0
        res = 0
        value = self.points.get(point[0])
        for (k, v) in value.items():
            if point[1] == k:
                continue
            d = abs(point[1] - k)
            x = point[0] - d
            if x in self.points.keys():
                y = self.points.get(x)
                value1 = y.get(k)
                value2 = y.get(point[1])
                if value1 is not None and value2 is not None:
                    res += v * value1 * value2
            x = point[0] + d
            if x in self.points.keys():
                y = self.points.get(x)
                value1 = y.get(k)
                value2 = y.get(point[1])
                if value1 is not None and value2 is not None:
                    res += v * value1 * value2

        return res









