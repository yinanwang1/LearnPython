from functools import cache
from math import inf
from typing import List

from sqlalchemy.dialects.mysql.base import MSInteger


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])

        @cache
        def dfs(i: int, j: int) -> int:
            # i 为机器人，j为工厂
            if i < 0:
                return 0
            if j < 0:
                return 2 ** 63 -1
            res = dfs(i, j - 1)
            position, limit = factory[j]
            sumDis = 0
            # i + 1 是指机器人的个数
            for k in range(1, min(i + 1, limit) + 1):
                # i+1-k是第几个机器人和工厂的距离。如第i个机器人，维修一个k=1个，则i + 1 - k = i.
                sumDis += abs(robot[i + 1 - k] - position)
                res = min(res, dfs(i - k, j - 1) + sumDis)

            return res

        return dfs(len(robot) - 1, len(factory) - 1)



if __name__ == '__main__':
    print(Solution().minimumTotalDistance([0,4,6], [[2,2],[6,2]]))






# 题解  https://leetcode.cn/problems/minimum-total-distance-traveled/solutions/1951947/ji-yi-hua-sou-suo-by-endlesscheng-qctr/?envType=daily-question&envId=2026-04-14&status=NOT_STARTED&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJBQ19SQVRFIn1d&difficulty=EASY
# 从右向左进行计算，重点是 当前的factory维修几个机器人，枚举可维修的机器人数量K。
# 每一个枚举K得到移动的总距离，取最小的。
# 例如K =0，就是当前工厂i不进行维修，那么总距离就是A = SUM(i-1)了。
# 当K=1，就是当前工厂i维修一个机器人，那么总距离就是B = SUM(i-1) + 机器人到工厂的距离。
# 判断A和B的大小，留下最小值。 依次类推K=2.。。