# There are n houses evenly lined up on the street, and each house is beautifully painted.
# You are given a 0-indexed integer array colors of length n, where colors[i] represents the color
# of the ith house.
# Return the maximum distance between two houses with different colors.
# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.


from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        p = 0
        q = len(colors) - 1
        l = colors[p]
        r = colors[q]
        while True:
            if l != colors[q] or r != colors[p]:
                break
            else:
                p += 1
                q -= 1

        return max(abs(0 - q), abs(len(colors) - 1 - p))
