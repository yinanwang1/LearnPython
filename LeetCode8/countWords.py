
# Given two string arrays words1 and words2, return the number of strings that appear exactly
# once in each of the two arrays.

from typing import List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        result = 0
        for (key, value) in dict(counter1).items():
            if value == 1 and 1 == counter2[key]:
                result += 1

        return result



