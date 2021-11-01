from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        max_depth = 0
        left = 0
        for character in seq:
            if character == '(':
                left += 1
            else:
                left -= 1

            max_depth = max(max_depth, left)

        middle = max_depth // 2

        result = list()
        odd_num = 0
        for character in seq:
            if character == '(':
                left += 1
            else:
                left -= 1

            if left <= middle and odd_num % 2 == 0:
                result.append(0)
                odd_num = 0
            else:
                result.append(1)
                odd_num += 1

        return result



