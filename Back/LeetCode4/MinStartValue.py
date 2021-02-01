from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        addList = [nums[0]]
        for value in nums[1:]:
            addList.append(addList[-1] + value)

        return 1 if min(addList) > 0 else abs(min(addList)) + 1