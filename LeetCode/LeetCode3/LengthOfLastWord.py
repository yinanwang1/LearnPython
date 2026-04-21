class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stringList = s.split(' ')
        result = list(filter(lambda x: x != '', stringList))
        if 0 == len(result):
            return 0

        return len(result[-1])