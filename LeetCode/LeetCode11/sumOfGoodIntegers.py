# 3954. 区间内的兼容数字之和 I
# https://leetcode.cn/problems/sum-of-compatible-numbers-in-range-i/description/?envType=problem-list-v2&envId=dynamic-programming


class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        ans = 0
        for i in range(max(0, n-k), n + k + 1):
            if n & i == 0:
                ans += i
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.sumOfGoodIntegers(1, 13))