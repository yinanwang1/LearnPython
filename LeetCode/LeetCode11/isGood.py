from typing import List


# 检查数组是否是好的
# https://leetcode.cn/problems/check-if-array-is-good/description/

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        if 2 > n:
            return False

        for i in range(n):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
            if i == n-1:
                return i == nums[i] and i == nums[i-1]
            else:
                if i + 1 != nums[i]:
                    return False

        return  True


if __name__ == '__main__':
    print(Solution().isGood(nums=[1, 3, 3, 2]))