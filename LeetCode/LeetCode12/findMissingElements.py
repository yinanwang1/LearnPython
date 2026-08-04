from typing import List


# 3731. 找出缺失的元素
# https://leetcode.cn/problems/find-missing-elements/

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans =[]
        pre = nums[0]-1
        for num in nums:
            minus = num - pre
            if 1 == minus:
                pre = num
                continue
            for v in range(1, minus):
                ans.append(pre + v)
            pre = num

        return ans




