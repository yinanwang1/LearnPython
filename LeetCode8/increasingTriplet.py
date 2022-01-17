# Given an integer array nums, return true if there exists a triple of
# indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false.


from typing import List

# [1,5,0,4,1,3]

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if 3 > len(nums):
            return False
        f = nums[0]
        s = f
        m = f
        foundS = False
        foundM = False
        for i in range(1, len(nums)):
            v = nums[i]
            if foundS:
                if v > s:
                    return True
                if f < v < s:
                    s = v
                elif v <= f:
                    if foundM:
                        if m < v:
                            f = v
                            s = m
                        else:
                            m = v
                    else:
                        foundM = True
                        m = v
            else:
                if v > f:
                    foundS = True
                    s = v
                else:
                    f = v

        return False
