from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None or len(nums) < 1:
            return 0

        index = 1
        preValue = nums[0]

        while index < len(nums):
            if preValue == nums[index]:
                del nums[index]
            else:
                preValue = nums[index]
                index += 1

        return len(nums)


