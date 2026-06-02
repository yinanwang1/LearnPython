from typing import List

# 3633. 最早完成陆地和水上游乐设施的时间 I
# https://leetcode.cn/problems/earliest-finish-time-for-land-and-water-rides-i/description/

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = 10 ** 5
        for i , v in enumerate(landStartTime):
            for j, w in enumerate(waterStartTime):
                end_time = v + landDuration[i]
                padding = w - end_time if w > end_time else 0
                ans = min(ans, end_time + padding + waterDuration[j])

                end_time = w + waterDuration[j]
                padding = v - end_time if v > end_time else 0
                ans = min(ans, end_time + padding + landDuration[i])

        return ans
