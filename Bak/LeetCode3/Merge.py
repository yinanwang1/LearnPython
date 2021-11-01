from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = 0
        leftTimes = 0
        while left < (m + n) and right < n:
            if nums1[left] > nums2[right]:
                nums1.insert(left, nums2[right])
                left += 1
                right += 1
            else:
                if leftTimes >= m:
                    nums1[left] = nums2[right]
                    left += 1
                    right += 1
                else:
                    left += 1
                    leftTimes += 1

        for _ in range(len(nums1) - m - n):
            nums1.pop(-1)