from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        wordL = ",".join(words)
        r = list()

        for w in words:
            if wordL.count(w) == 1:
                r.append(w)

        return r
