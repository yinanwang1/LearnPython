# LCS 01. 下载插件
# https://leetcode.cn/problems/Ju9Xwi/description/


class Solution:
    def leastMinutes(self, n: int) -> int:
        times = 1
        current = 1
        while current < n:
            times += 1
            current *= 2

        return min(n, times + 1)


if __name__ == '__main__':
    print(Solution().leastMinutes(n=10))
