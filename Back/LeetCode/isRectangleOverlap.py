from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec2[0] < rec1[2] and rec2[1] < rec1[3] and rec2[2] > rec1[0] and rec2[3] > rec1[1]:
            return True

        return False




solution = Solution()
result = solution.isRectangleOverlap([-687153884,-854669644,-368882013,-788694078], [540420176,-909203694,655002739,-577226067])
print('END')
print(result)


