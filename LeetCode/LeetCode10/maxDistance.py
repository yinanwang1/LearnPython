from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        res = 0
        i = 0
        for j in range(n2):
            while i < n1 and nums1[i] > nums2[j]:
                i += 1
            if i < n1:
                res = max(res, j - i)
        return res


if __name__ == '__main__':
    print(Solution().maxDistance([55,30,5,4,2], [100,20,10,10,5]))