class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or s == "":
            return True

        while s.count('()') > 0 or s.count('{}') > 0 or s.count('[]') > 0:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')

        return 0 >= len(s)


