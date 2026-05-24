from functools import cache
from typing import List


# 1340. 跳跃游戏 V
# https://leetcode.cn/problems/jump-game-v/description/

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        length = len(arr)

        @cache
        def dfs(index: int):
            l = max(0, index - d)
            r = min(length - 1, index + d)
            next_index = []
            for leftIndex in range(index -1, l-1, -1):
                if arr[leftIndex] >= arr[index]:
                    break
                next_index.append(leftIndex)
            for j in range(index +1, r + 1):
                if arr[j] >= arr[index]:
                    break
                next_index.append(j)
            if not next_index:
                return 1
            return 1 + max(dfs(k) for k in next_index)

        result = 0
        for i in range(len(arr)):
            result = max(result, dfs(i))

        return result


if __name__ == '__main__':
    # print(Solution().maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2))
    # print(Solution().maxJumps([3,3,3,3,3], 3))
    print(Solution().maxJumps([22,29,52,97,29,75,78,2,92,70,90,12,43,17,97,18,58,100,41,32], 17))
