from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        right_sum = [0]
        n = len(nums)
        for i in range(1, len(nums)):
            left_sum.append(left_sum[i - 1] + nums[i - 1])
            right_sum.insert(0, right_sum[0] + nums[n - i])
        ans = []
        for i in range(n):
            ans.append(abs(left_sum[i] - right_sum[i]))

        return ans


if __name__ == '__main__':
    print(Solution().leftRightDifference([10, 4, 8, 3]))
