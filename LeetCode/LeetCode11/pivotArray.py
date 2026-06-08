from typing import List


# 2161. 根据给定数字划分数组
# https://leetcode.cn/problems/partition-array-according-to-given-pivot/description/



class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pre_list = []
        equal_list = []
        post_list = []
        for num in nums:
            if num < pivot:
                pre_list.append(num)
            elif num == pivot:
                equal_list.append(num)
            else:
                post_list.append(num)
        return pre_list + equal_list + post_list

