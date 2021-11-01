from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for index, value in enumerate(nums):
            s = n - index
            if value >= s:
                left = max(0, index - 1)
                if s > left:
                    return s

        return -1
