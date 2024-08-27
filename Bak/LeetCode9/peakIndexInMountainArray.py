# 符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：
#
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 的下标 i ，即山峰顶部。

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = len(arr)
        left, right = 0, l - 1
        while True:
            mid = (left + right) // 2
            v = arr[mid]
            if arr[mid - 1] < v and v > arr[mid + 1]:
                return mid
            if arr[mid - 1] < v:
                left = mid + 1
            else:
                right = mid - 1