
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        charMap = dict()
        for c in s:
            d = charMap.get(c, 0)
            if d >= 2:
                return c
            charMap[c] = d + 1

        return ""
