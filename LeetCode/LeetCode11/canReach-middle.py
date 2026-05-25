# 1871. 跳跃游戏 VII
# https://leetcode.cn/problems/jump-game-vii/description/


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        sum_pre = [0] * (n + 1)
        sum_pre[1] = 1
        value = True
        for i in range(1, n):
            value = i >= minJump and '0'==s[i] and sum_pre[max(i - minJump + 1, 0)] - sum_pre[max(i - maxJump, 0)]
            sum_pre[i + 1] = sum_pre[i] + value

        return True if value else False 


if __name__ == '__main__':
    print(Solution().canReach(s="011010", minJump=2, maxJump=3))
    # print(Solution().canReach(s="01101110", minJump=2, maxJump=3))
