from typing import List

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        value = K + int("".join([str(x) for x in A]))
        return [int(x) for x in list(str(value))]
