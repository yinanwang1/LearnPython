from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if val == nums[index]:
                del nums[index]
            else:
                index += 1

        return len(nums)
