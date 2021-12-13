# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
# 实现 Solution class:
# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果
import copy
import math
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.origin_nums = nums
        self.shuffle_nums = None
        self.r = random.Random()

    def reset(self) -> List[int]:
        self.shuffle_nums = None

        return self.origin_nums

    def shuffle(self) -> List[int]:
        if self.shuffle_nums is not None:
            return self.shuffle_nums

        length = len(self.origin_nums)
        self.shuffle_nums = self.origin_nums[:]
        for index in range(length):
            i = math.floor(self.r.random() * (index + 1))
            t = self.shuffle_nums[i]
            self.shuffle_nums[i] = self.shuffle_nums[index]
            self.shuffle_nums[index] = t

        return self.shuffle_nums
