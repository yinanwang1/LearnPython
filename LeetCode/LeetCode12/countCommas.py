# 3871. 统计范围内的逗号 II
# https://leetcode.cn/problems/count-commas-in-range-ii/description/


class Solution1:
    def countCommas(self, n: int) -> int:
        n_str = str(n)
        length = len(n_str)
        if 3 >= length:
            return 0

        def commasOfLength(l: int) -> int:
            return (l - 1) // 3

        commas_length_count = {x: commasOfLength(x) for x in range(1, length + 1)}
        ans = 0
        for i in range(4, length):
            ans += commas_length_count[i] * (10 ** (i - 1)) * 9
        ans += commas_length_count[length] * (10 ** (length - 1)) * (int(n_str[0]) - 1)
        ans += commas_length_count[length] * (int(n_str[1:]) + 1)

        return ans


# 另一种思路.  每一个逗号贡献的次数
class Solution:
    def countCommas(self, n: int) -> int:
        p = 1000
        ans = 0
        while p <= n:
            ans += n - p + 1
            p *= 1000
        return ans


if __name__ == '__main__':
    solution = Solution()

    print(solution.countCommas(10028999))
