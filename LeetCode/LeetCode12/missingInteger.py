from itertools import pairwise
from typing import List


# 2996. 大于等于顺序前缀和的最小缺失整数
# https://leetcode.cn/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        for s, t in pairwise(nums):
            if 1 == t - s:
                total += t
            else:
                break
        nums_set = set(nums)
        while total in nums_set:
            total += 1

        return total



if __name__ == '__main__':
    nums = [18,19,20,21,22,23,24,25,26,27,28,9]
    # nums = [4,5,6,7,8,8,9,4,3,2,7]
    solution = Solution()
    print(solution.missingInteger(nums))