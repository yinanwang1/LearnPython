


# 1358. 包含所有三种字符的子字符串数目
# https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        pre = [[0] * (n + 1) for _ in range(3)]
        for i in range(n):
            for j in range(3):
                pre[j][i + 1] = pre[j][i]
            pre[ord(s[i]) - ord('a')][i + 1] += 1

        for i in range(n):
            left, right = i + 1, n
            pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if pre[0][mid] - pre[0][i] > 0 and pre[1][mid] - pre[1][i] > 0 and pre[2][mid] - pre[2][i] > 0:
                    right = mid - 1
                    pos = mid
                else:
                    left = mid + 1
            if -1 != pos:
                ans += n - pos + 1

        return ans

if __name__ == '__main__':
    print(Solution().numberOfSubstrings("abcabc"))
