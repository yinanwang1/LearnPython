from typing import List
# 2029. 石子游戏 IX
# https://leetcode.cn/problems/stone-game-ix/description/

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for val in stones:
            if 0 == (typ := val % 3):
                cnt0 += 1
            elif typ == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
        return cnt1 - cnt2 > 2 or cnt2 - cnt1 > 2


# 这个是思考题啊。 如果思路想到了，那么写代码是有手就行。