import math


# 3867. 数对的最大公约数之和
# https://leetcode.cn/problems/sum-of-gcd-of-formed-pairs/


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_value = nums[0]
        prefixGcd = list()
        for num in nums:
            max_value = max(max_value, num)
            prefixGcd.append(math.gcd(num, max_value))
        prefixGcd = sorted(prefixGcd)
        ans = 0
        length = len(prefixGcd)
        for i in range(length // 2):
            ans += math.gcd(prefixGcd[i], prefixGcd[length - 1 - i])

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.gcdSum([3,6,2,8]))