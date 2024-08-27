
# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values
# that are present in at least two out of the three arrays. You may return the values in any order.


from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1Set, nums2Set, nums3Set = set(nums1), set(nums2), set(nums3)
        set1 = nums1Set.intersection(nums2Set)
        set2 = nums2Set.intersection(nums3Set)
        set3 = nums3Set.intersection(nums1Set)
        set1.update(set2)
        set1.update(set3)

        return list(set1)

