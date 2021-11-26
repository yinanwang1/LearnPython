from typing import List

class Solution:
    def permutation(self, S: str) -> List[str]:
        result = set()

        def recursion(path: str, chars: List[str]):
            if 0 >= len(chars):
                result.add(path)
                return

            for i, v in enumerate(chars):
                recursion(path + v, chars[:i] + chars[i+1:])

        recursion('', list(S))


        return list(result)
