from typing import List

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        index_list = list()

        for index, character in enumerate(S):
            if character == C:
                index_list.append(index)

        result = list()
        for index, character in enumerate(S):
            distance = map(lambda x: abs(x - index), index_list)
            result.append(min(distance))

        return result