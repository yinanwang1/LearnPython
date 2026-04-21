from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """

        def move(n: int, a: List[int], b: List[int], c: List[int]):
            if n == 1:
                c.append(a.pop())
                return

            move(n - 1, a, c, b)
            c.append(a.pop())
            move(n - 1, b, a, c)

        n = len(A)
        move(n, A, B, C)

