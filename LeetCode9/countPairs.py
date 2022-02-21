
# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j)
# where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # 遍历一次将所有相同的值的索引放一起
        indexDic = dict()
        for i, v in enumerate(nums):
            if v not in indexDic.keys():
                indexDic.setdefault(v, [i])
            else:
                indexList = indexDic.get(v)
                indexList.append(i)

        res = 0
        for v, indexList in indexDic.items():
            length = len(indexList)
            if 1 >= length:
                continue
            for i in range(length):
                for j in range(i + 1, length):
                    if indexList[i] * indexList[j] / k == 0:
                        res += 1

        return res






