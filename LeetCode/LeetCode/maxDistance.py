from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        length = len(grid)
        counts = [[0] * length for _ in range(length)]

        for i in range(length):
            for j in range(length):
                if 1 == grid[i][j]:
                    counts[i][j] = 0
                else:
                    if i - 1 >= 0 and j - 1 >= 0:
                        counts[i][j] = min(counts[i - 1][j], counts[i][j - 1]) + 1
                    elif i - 1 >= 0:
                        counts[i][j] = counts[i - 1][j] + 1
                    elif j - 1 >= 0:
                        counts[i][j] = counts[i][j - 1] + 1
                    else:
                        counts[i][j] = 2 * length

        reverse_range = list(range(length))[::-1]
        for i in reverse_range:
            for j in reverse_range:
                if 1 == grid[i][j]:
                    counts[i][j] = 0
                else:
                    if i + 1 < length and j + 1 < length:
                        counts[i][j] = min(counts[i + 1][j] + 1, counts[i][j + 1] + 1, counts[i][j])
                    elif i + 1 < length:
                        counts[i][j] = min(counts[i + 1][j] + 1, counts[i][j])
                    elif j + 1 < length:
                        counts[i][j] = min(counts[i][j + 1] + 1, counts[i][j])
                    else:
                        counts[i][j] = counts[i][j]

        max_value = 0

        for item in counts:
            max_value = max(max_value, max(item))

        return max_value if max_value != 0 and max_value < 2 * length else -1

