from typing import List

from SnippetCode.gps_transfomer import count


# 1306. 跳跃游戏 III
# https://leetcode.cn/problems/jump-game-iii/description/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        found_list = [0] * n
        queue = [start]
        while 0 < len(queue):
            temp = []
            for i in queue:
                if 0 > i or i >= n:
                    continue
                if 1 == found_list[i]:
                    continue
                if 0 == arr[i]:
                    return True
                found_list[i] = 1
                temp.append(i - arr[i])
                temp.append(i + arr[i])

            queue = temp

        return False


if __name__ == '__main__':
    print(Solution().canReach([4,2,3,0,3,1,2], 5))
