from typing import List


# 1674. 使数组互补的最少操作次数
# https://leetcode.cn/problems/minimum-moves-to-make-array-complementary/description/
# 差分数组 的含义 https://app.yinxiang.com/shard/s31/nl/6475400/b8e59f8d-b914-4907-9c8c-16ed4f858ae5/

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1- i])

            diff[2] += 2
            diff[a + 1] += -2 + 1
            diff[a + b] += -1
            diff[a + b + 1] += 1
            diff[b + limit + 1] += -1 + 2

        res = n
        current = 0
        for i in range(2, 2 * limit + 1):
            current += diff[i]
            if current < res:
                res = current

        return res





if __name__ == '__main__':
    # print(Solution().minMoves([28,50,76,80,64,30,32,84,53,8], 84))
    # print(Solution().minMoves([20744, 7642, 19090, 9992, 2457, 16848, 3458, 15721], 22891))
    print(Solution().minMoves([1,3,1,1,1,2,3,2,3,1,3,2,1,3], 3))
