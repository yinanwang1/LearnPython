from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        chars = set(list(A[0]))
        chars_count = list()
        result = list()

        from collections import Counter
        for string in A:
            c = Counter(string)
            chars_count.append(dict(c))

        for character in chars:
            nums = list()
            for diction in chars_count:
                nums.append(diction.get(character, 0))

            for _ in range(min(nums)):
                result.append(character)

        return result




