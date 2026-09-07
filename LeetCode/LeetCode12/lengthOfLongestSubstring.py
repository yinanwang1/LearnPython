# 3. 无重复字符的最长子串
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        chars = {s[0]}
        left, right, max_length = 0, 1, 1
        while left < right < n:
            char = s[right]
            if char in chars:
                chars.remove(s[left])
                left += 1
                if left == right:
                    chars.add(s[left])
                    right += 1
            else:
                chars.add(char)
                right += 1
                max_length = max(max_length, right - left)

        return max_length


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("bbbbbb"))
