from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        distanceList = list()
        index = -1

        for i, v in enumerate(nums):
            if v == 1:
                if index == -1:
                    index = i
                else:
                    distanceList.append(i - index - 1)
                    index = i

        return k <= min(distanceList)