

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        for key, value in ransomCounter.items():
            if key not in magazineCounter.keys():
                return False
            if value > magazineCounter.get(key):
                return False

        return True

