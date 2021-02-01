from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsTemp = sorted(nums)
        result = list()

        for num in nums:
            result.append(numsTemp.index(num))

        return result

