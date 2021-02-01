from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        c = dict(Counter(arr))

        result = -1

        for key, value in c.items():
            if key == value:
                result = max(result, key)

        return result


