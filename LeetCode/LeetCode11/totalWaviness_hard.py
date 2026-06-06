from functools import cache, lru_cache


# 3753. 范围内总波动值 II
# https://leetcode.cn/problems/total-waviness-of-numbers-in-range-ii/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(num: int) -> int:
            if 100 >= num:
                return 0

            num_str = str(num)
            n = len(num_str)

            @lru_cache
            def dfs(pos: int, pre: int, curr: int, isLimit: bool, isLeading: bool) -> tuple[int, int]:
                if n == pos:
                    return 1, 0
                cnt = 0
                waviness = 0
                up = int(num_str[pos]) if isLimit else 9
                for digit in range(up + 1):
                    newLeading = isLeading and (0 == digit)
                    newPre = curr
                    newCurr = -1 if newLeading else digit
                    new_cnt, new_sum = dfs(pos + 1, newPre, newCurr, isLimit and (up == digit), newLeading)
                    if not newLeading and pre > 0 and curr > 0:
                        if pre < curr > digit or pre > curr < digit:
                            waviness += new_cnt
                    cnt += new_cnt
                    waviness += new_sum

                return cnt, waviness

            _, cnt_sum = dfs(0, -1, -1, True, True)

            return cnt_sum

        return solve(num2) - solve(num1 - 1)






if __name__ == '__main__':
    # print(Solution().totalWaviness(num1 = 120, num2 = 130))
    print(Solution().totalWaviness(num1 = 1, num2 = 1000000000000))
