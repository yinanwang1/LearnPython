# 你是一个专业的小偷，计划偷窃沿街的房屋。
# 每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        max_index = len(nums) - 1
        # 0 不包含 1 包含
        values = [[0] * 2 for row in range(len(nums))]
        values[0][1] = nums[0]
        for i in range(1, len(nums)):
            values[i][0] = max(values[i - 1][0], values[i - 1][1])
            values[i][1] = max(values[i - 1][0] + nums[i], values[i - 1][1])

        return max(values[max_index][0], values[max_index][1])
