# A sentence is a list of words that are separated by a single
# space with no leading or trailing spaces.
# You are given an array of strings sentences, where each
# sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.

from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for s in sentences:
            count = max(count, len(s.split(" ")))

        return count


