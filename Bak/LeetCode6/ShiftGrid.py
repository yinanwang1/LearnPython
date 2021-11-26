from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid[0])
        m = len(grid)
        k = k % (n * m)
        allList = list()
        for v in grid:
            allList.extend(v)
        shift = allList[-k:]
        shift.extend(allList[:-k])
        result = list()
        print(shift)
        index = 0
        while index < len(shift):
            result.append(shift[index:n + index])
            index += n

        return result
