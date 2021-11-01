from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        index = 0

        while index < len(nums):
            length = 1
            found = False
            while True:
                if index + length >= len(nums):
                    break

                if nums[index + length] >= length:
                    index += length
                    found = True
                    break

                length += 1

            if not found:
                if index + length >= len(nums):
                    break

        return index == len(nums) - 1
