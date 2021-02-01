from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        c = Counter(deck)
        count_set = set()
        for _, value in dict(c).items():
            count_set.add(value)

        for value in range(2, min(count_set) + 1):
            result = True
            for count in count_set:
                if count % value != 0:
                    result = False
                    break

            if result:
                return True

        return False