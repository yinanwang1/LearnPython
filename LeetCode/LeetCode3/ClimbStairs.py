class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        p = 1
        q = 2
        index = 2
        while index < n:
            index += 1
            t = q
            q = p + q
            p = t

        return p + q

