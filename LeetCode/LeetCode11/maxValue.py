from itertools import accumulate
from typing import List



# 3660. 跳跃游戏 IX
# https://leetcode.cn/problems/jump-game-ix/description/


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_max = list(accumulate(nums, max))
        suf_min = 10 ** 10
        for i in range(n-1, -1, -1):
            if pre_max[i] > suf_min:
                pre_max[i] = pre_max[i+1]
            suf_min = min(suf_min, nums[i])
        return pre_max


if __name__ == '__main__':
    s = Solution()
    print(s.maxValue([2,3,1]))