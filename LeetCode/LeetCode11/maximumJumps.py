from functools import cache
from math import inf
from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-inf] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        ans = dp[n-1]

        return int(-1 if ans < 0 else ans)


if __name__ == '__main__':
    print(Solution().maximumJumps(nums = [1,3,6,4,1,2], target = 2))