from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for query in queries:
            for dic in dictionary:
                times = 0
                for i in range(len(query)):
                    if query[i] != dic[i]:
                        times += 1
                        if times > 2:
                            break
                else:
                    res.append(query)
                    break
        return res

