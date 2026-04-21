
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # 将所有单词按长度放入字典中
        wordLength = {i: list() for i in range(1, 31)}
        for w in words:
            l = len(w)
            wordLength.get(l).append(w)

        resList = wordLength.get(1)
        if 0 >= len(resList):
            return ""
        resList.sort()
        longest = resList[0]
        for i in range(2, 31):
            iList = wordLength.get(i)
            temp = list()
            for w in iList:
                if w[:-1] in resList:
                    temp.append(w)
            temp.sort()
            resList = temp
            if len(temp) > 0:
                longest = resList[0]
            else:
                break

        return longest
