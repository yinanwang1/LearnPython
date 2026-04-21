
# Two strings word1 and word2 are considered almost equivalent if the differences
# between the frequencies of each letter
# from 'a' to 'z' between word1 and word2 is at most 3.
# Given two strings word1 and word2, each of length n,
# return true if word1 and word2 are almost equivalent, or false otherwise.
# The frequency of a letter x is the number of times it occurs in the string.



class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        counter1 = dict(Counter(word1))
        counter2 = dict(Counter(word2))
        all = set(counter1.keys()).union(set(counter2.keys()))
        for c in all:
            num1 = counter1.get(c) if counter1.get(c) else 0
            num2 = counter2.get(c) if counter2.get(c) else 0
            if abs(num2 - num1) > 3:
                return False

        return True

