from typing import List

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words = A.split(' ') + B.split(' ')
        from collections import Counter
        nums = dict(Counter(words))
        result = list()
        for key, value in nums.items():
            if value == 1:
                result.append(key)

        return result
