from typing import List


# 2657. 找到两个数组的前缀公共数组
# https://leetcode.cn/problems/find-the-prefix-common-array-of-two-arrays/description/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        different_left_list = []
        different_right_list = []
        for i in range(n):
            if A[i] == B[i]:
                if 0 == i:
                    ans[i] = 1
                else:
                    ans[i] = ans[i -1] + 1
            else:
                sames = 0
                if A[i] in different_right_list:
                    sames += 1
                    different_right_list.remove(A[i])
                else:
                    different_left_list.append(A[i])
                if B[i] in different_left_list:
                    sames += 1
                    different_left_list.remove(B[i])
                else:
                    different_right_list.append(B[i])
                if 0 == i:
                    ans[i] = sames
                else:
                    ans[i] = ans[i - 1] + sames

        return ans


