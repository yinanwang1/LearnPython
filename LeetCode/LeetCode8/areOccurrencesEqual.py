# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences
# (i.e., the same frequency).

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        counter = Counter(s)
        sSet = set(counter.values())

        return 1 == len(sSet)

