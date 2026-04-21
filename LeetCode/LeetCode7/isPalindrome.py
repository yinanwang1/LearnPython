# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        t = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l = 0
        r = len(t) - 1
        while l < r:
            if t[l] != t[r]:
                return False
            l += 1
            r -= 1

        return True
