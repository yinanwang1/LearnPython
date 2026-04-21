from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minus = 0
        while True:
            left = start - minus
            right = start + minus
            if left >= 0 and nums[left] == target:
                return minus
            if right < len(nums) and nums[right] == target:
                return minus
            minus += 1


