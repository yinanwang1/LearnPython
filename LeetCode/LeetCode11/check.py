from typing import List


# 1752. 检查数组是否经排序和轮转得到
# https://leetcode.cn/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        x = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                x = i
                break
        if x == 0:
            return True
        for i in range(x + 1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return nums[0] >= nums[-1]


if __name__ == '__main__':
    # print(Solution().check(nums = [3,4,5,1,2]))
    # print(Solution().check(nums = [1,2,3]))
    print(Solution().check(nums = [6,10,6]))
