from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        from collections import Counter
        result = 0

        for word in words:
            counter = Counter(word)
            all_in = True
            for char in dict(counter).keys():
                if char not in allowed:
                    all_in = False
                    break
            if all_in:
                result += 1

        return result

