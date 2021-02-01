from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        targets = list()

        for i in range(len(nums)):
            if index[i] >= len(targets):
                targets.append(nums[i])
            else:
                targets.insert(index[i], nums[i])

        return targets