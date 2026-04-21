class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        numsDic = dict()
        for index, char in enumerate(s):
            value = numsDic.get(char, list())
            value.append(index)
            numsDic[char] = value

        maxValue = -1
        for key, value in numsDic.items():
            if 2 > len(value):
                continue

            maxValue = max(maxValue, max(value) - min(value) - 1)

        return maxValue
