from typing import List
from functools import reduce

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        value1 = reduce(lambda x, y: x * y, nums[-3:])
        value2 = reduce(lambda x, y: x * y, nums[:3])
        value3 = nums[0] * nums[-1] * nums[-2]

        return max(value1, value2, value3)



