from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        index_list = [(index, len(x)) for index, x in enumerate(words)]
        index_list.sort(key=lambda x: x[1], reverse=True)
        S = ""
        indexes = [0] * len(words)

        for index, _ in index_list:
            word = words[index] + '#'
            try:
                word_index = S.index(word)
                indexes[index] = word_index
            except ValueError:
                indexes[index] = len(S)
                S += word

        return len(S)



