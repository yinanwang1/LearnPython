# 给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。
# 实现 MovingAverage 类：
# MovingAverage(int size) 用窗口大小 size 初始化对象。
# double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，
# 请计算并返回数据流中最后 size 个值的移动平均值，即滑动窗口里所有数字的平均值。


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.total = 0
        self.nums = []

    def next(self, val: int) -> float:
        self.total += val
        self.nums.append(val)
        if len(self.nums) > self.size:
            self.total -= self.nums.pop(0)

        return float(self.total / len(self.nums))
