from typing import List


# 2900. 最长相邻不相等子序列 I
# https://leetcode.cn/problems/longest-unequal-adjacent-groups-subsequence-i/description/?envType=problem-list-v2&envId=dynamic-programming

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        begin_zero = []
        begin_zero_need = 0
        begin_one = []
        begin_one_need = 1
        for i, v in enumerate(groups):
            if v == begin_zero_need:
                begin_zero.append(words[i])
                begin_zero_need = (begin_zero_need + 1) % 2
            if v == begin_one_need:
                begin_one.append(words[i])
                begin_one_need = (begin_one_need + 1) % 2
        return begin_zero if len(begin_zero) > len(begin_one) else begin_one

if __name__ == '__main__':
    solution = Solution()
    print(solution.getLongestSubsequence(["h","vv","kp"], [0,1,0]))