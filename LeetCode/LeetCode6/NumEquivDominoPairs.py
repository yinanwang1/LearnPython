from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = 0
        index = 0
        while index < len(dominoes) - 1:
            i = index + 1
            same = 1
            while i < len(dominoes):
                x, y = dominoes[index]
                a, b = dominoes[i]
                print('x is ' + str(x) + ' y is ' + str(y))
                print('a is ' + str(a) + ' b is ' + str(b))
                if (x == a and y == b) or (x == b and y == a):
                    same += 1
                    dominoes.pop(i)
                else:
                    i += 1

            print(same)

            if same > 1:
                pairs += int(same * (same - 1) / 2)

            index += 1

        return pairs
