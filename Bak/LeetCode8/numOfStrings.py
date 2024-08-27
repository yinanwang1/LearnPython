# Given an array of strings patterns and a string word, return the number of strings
# in patterns that exist as a substring in word.
# A substring is a contiguous sequence of characters within a string.


from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for p in patterns:
            try:
                word.index(p)
                result += 1
            except ValueError:
                continue

        return result

