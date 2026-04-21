from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(indices)
        for i in range(0, len(indices)):
            index = indices[i]
            result[index] = s[i]

        return ''.join(result)