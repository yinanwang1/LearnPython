from functools import reduce
from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10 ** 9 + 7)
                idx += k
        return reduce(lambda x, y: x ^ y, nums, 0)








