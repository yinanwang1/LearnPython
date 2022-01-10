# Given an integer array nums, return the greatest common divisor of the smallest
# number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer
# that evenly divides both numbers.

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        left = nums[0]
        right = nums[-1]
        while True:
            y = right % left
            if y == 0:
                return left
            else:
                right = left
                left = y
