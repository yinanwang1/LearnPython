from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        left = []
        right = []

        for item in paths:
            left.append(item[0])
            right.append(item[1])

        from collections import Counter
        counter = Counter(left + right)
        for key, value in dict(counter).items():
            if value == 1:
                try:
                    left.index(key)
                except:
                    return key
