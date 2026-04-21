class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(list(map(lambda x: ord(x), t))) - sum(s'holist(map(lambda x: ord(x), s))))