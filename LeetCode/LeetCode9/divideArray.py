
# You are given an integer array nums consisting of 2 * n integers.
#
# You need to divide nums into n pairs such that:
#
# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.


from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        counter = Counter(nums)
        for v in counter.values():
            if 0 != v % 2:
                return False

        return True