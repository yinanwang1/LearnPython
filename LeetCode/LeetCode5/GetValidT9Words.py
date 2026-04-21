from typing import List

class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        keys = {'2':['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}

        wordsResult = words.copy()
        for index, char in enumerate(num):
            wordsTemp = list()
            for word in wordsResult:
                if word[index] in keys.get(char, []):
                    wordsTemp.append(word)
            wordsResult = wordsTemp

        return wordsResult