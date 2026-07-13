from typing import List


# 1331. 数组序号转换
# https://leetcode.cn/problems/rank-transform-of-an-array/description/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        order_arr = sorted(set(arr))
        order_map = {}
        index = 1
        for v in order_arr:
            order_map[v] = index
            index += 1

        return [order_map[x] for x in arr]