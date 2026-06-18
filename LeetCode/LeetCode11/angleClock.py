
# 1344. 时钟指针的夹角
# https://leetcode.cn/problems/angle-between-hands-of-a-clock/


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_degree = 360 * minutes / 60
        hour_degree = 360 * hour / 12 + 30 * minutes / 60
        distance = abs(minutes_degree - hour_degree)

        return min(distance, abs(360 - distance))
