from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = colors[0], colors[-1]
        length = len(colors)
        for index in range((length + 1) // 2):
            if left != colors[length - 1 - index] or right != colors[index]:
                return length - 1 - index

        return 0


