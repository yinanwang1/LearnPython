class Solution:
    def firstUniqChar(self, s: str) -> str:
        singleChars = list()
        multiChars = list()
        for char in s:
            if char in multiChars:
                continue
            if char not in singleChars:
                singleChars.append(char)
            else:
                singleChars.remove(char)
                multiChars.append(char)

        return singleChars[0] if singleChars else ' '