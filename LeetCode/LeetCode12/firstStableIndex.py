from math import inf


# 3904. 最小稳定下标 II
# https://leetcode.cn/problems/smallest-stable-index-ii/description/


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        length = len(nums)
        min_value_list = [inf] * (length - 1) + [nums[-1]]

        for i in range(length - 2, -1, -1):
            min_value_list[i] = min(nums[i], min_value_list[i + 1])

        max_value = nums[0]
        for i, v in enumerate(nums):
            max_value = max(max_value, v)
            if max_value - min_value_list[i] <= k:
                return i
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstStableIndex([5,0,1,4], 3))

