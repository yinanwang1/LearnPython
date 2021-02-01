from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        chars = dict()
        for char in licensePlate.lower():
            if char.isalpha():
                value = chars.get(char, 0)
                chars[char] = value + 1

        result = None
        for word in words:
            for key, value in chars.items():
                if value > word.count(key):
                    break
            else:
                if result:
                    result = word if len(word) < len(result) else result
                else:
                    result = word

        return result
