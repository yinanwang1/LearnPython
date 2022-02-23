
# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
#
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
import math


class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                v = math.sqrt(i * i + j * j)
                if v == int(v) and v <= n:
                    res += 1

        return res * 2


def main():
    for i in range(1, 100000):
        v = math.sqrt(i * i + i * i)
        if v == int(v):
            print("i is {}, v is {}".format(i, v))
            break


if __name__ == '__main__':
    main()