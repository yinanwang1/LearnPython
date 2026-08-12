from typing import List, Counter


# 2958. 最多 K 个重复元素的最长子数组
# https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n, counter = len(nums), Counter()
        right, ans = -1, 0
        for left in range(n):
            if left > 0:
                counter[nums[left - 1]] -= 1
            while right + 1 < n and counter[nums[right + 1]] < k:
                right += 1
                counter[nums[right]] += 1

            ans = max(ans, right - left + 1)

        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubarrayLength([1,2,3,1,2,3,1,2], 2))