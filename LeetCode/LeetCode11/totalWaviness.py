# 3751. 范围内总波动值 I
# https://leetcode.cn/problems/total-waviness-of-numbers-in-range-i/description/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def calc(num: int) -> int:
            num_str = str(num)
            n = len(num_str)
            if 3 > n:
                return 0
            ans = 0
            for i in range(1, n - 1):
                if int(num_str[i - 1]) < int(num_str[i]) > int(num_str[i + 1]):
                    ans += 1
                elif int(num_str[i - 1]) > int(num_str[i]) < int(num_str[i + 1]):
                    ans += 1

            return ans

        return sum([calc(v) for v in range(num1, num2 + 1)])


if __name__ == '__main__':
    print(Solution().totalWaviness(num1 = 100, num2 = 999))
