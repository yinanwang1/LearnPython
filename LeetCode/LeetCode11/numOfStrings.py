from typing import List

# 1967. 作为子字符串出现在单词中的字符串数目
# https://leetcode.cn/problems/number-of-strings-that-appear-as-substrings-in-word/description/


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 for pattern in patterns if pattern in word])