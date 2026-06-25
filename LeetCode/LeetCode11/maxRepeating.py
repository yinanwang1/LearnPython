

# 1668. 最大重复子字符串
# https://leetcode.cn/problems/maximum-repeating-substring/description/?envType=problem-list-v2&envId=dynamic-programming



class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        l = len(sequence)
        n = len(word)
        for i, c in enumerate(sequence):
            if c != word[0]:
                continue
            k = 0
            for j in range(i, l, n):
                end = min(l, j+n)
                if sequence[j: end] == word:
                    k += 1
                else:
                    break
            res = max(res, k)

        return res







