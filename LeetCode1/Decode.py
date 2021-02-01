from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for index, value in enumerate(encoded):
            result.append(result[-1] ^ value)

        return result

