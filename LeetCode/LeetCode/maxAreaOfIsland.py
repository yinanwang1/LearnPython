from typing import List


class Solution:
    def __init__(self):
        self.island = set()

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        island_set = set()
        max_i = len(grid)
        max_j = len(grid[0])

        def is_island(i: int, j: int):
            if i < 0 or j < 0 or i >= max_i or j >= max_j:
                return

            if 1 == grid[i][j]:
                if (i, j) in island_set:
                    return

                self.island.add((i, j))
                island_set.add((i, j))
                if (i - 1, j) not in self.island:
                    is_island(i - 1, j)
                if (i + 1, j) not in self.island:
                    is_island(i + 1, j)
                if (i, j - 1) not in self.island:
                    is_island(i, j - 1)
                if (i, j + 1) not in self.island:
                    is_island(i, j + 1)

        for index_i in range(len(grid)):
            for index_j in range(len(grid[0])):
                self.island.clear()
                is_island(index_i, index_j)

                max_island = max(max_island, len(self.island))

        return max_island



solution = Solution()
result = solution.maxAreaOfIsland([[0,1]])

print(result)