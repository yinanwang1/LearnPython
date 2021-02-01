from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()

        def recursion(state, p, q):
            if p > q:
                return
            if p == 0 and q == 0:
                result.append(state)
                return

            if p > 0:
                recursion(state + '(', p - 1, q)

            if q > 0:
                recursion(state + ')', p, q - 1)

        recursion('', n, n)

        return result








