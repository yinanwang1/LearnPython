class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        char_count = dict(Counter(s))
        single = False
        length = 0

        for key, value in char_count.items():
            length += value if value % 2 == 0 else value - 1

            if value % 2 != 0 and not single:
                single = True

        return length if not single else length + 1

