# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.


from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairIndex, result, lengthNum1, lengthNum2 = [0] * len(nums1), [], len(nums1), len(nums2)
        while len(result) < k:
            for i, v in enumerate(pairIndex):
                if v != lengthNum2:
                    index1, index2 = i, v
                    break
            else:
                break

            for i in range(index1 + 1, lengthNum1):
                v = pairIndex[i]
                if v >= lengthNum2:
                    continue
                if nums1[index1] + nums2[index2] > nums1[i] + nums2[v]:
                    index1, index2 = i, v

                if 0 == v:
                    break

            pairIndex[index1] = index2 + 1
            result.append([nums1[index1], nums2[index2]])

        return result
