
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1：
#
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 示例 2:
#
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
#
# 交集可能是重复的数字
#
#

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        nums1.sort()
        nums2.sort()

        index1 = 0
        nums1Len = len(nums1)
        index2 = 0
        nums2Len = len(nums2)

        while index1 < nums1Len and index2 < nums2Len:
            if nums1[index1] == nums2[index2]:
                result.append(nums1[index1])
                index1 += 1
                index2 += 1
            else:
                if nums1[index1] < nums2[index2]:
                    index1 += 1
                else:
                    index2 += 1

        return result
