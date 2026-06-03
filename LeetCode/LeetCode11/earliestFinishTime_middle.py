from typing import List

# 最早完成陆地和水上游乐设施的时间 II
# https://leetcode.cn/problems/earliest-finish-time-for-land-and-water-rides-ii/

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def earliestTime(firstStartTime: List[int], firstDuration: List[int], secondStartTime: List[int], secondDuration: List[int]) -> int:
            firstEarly = 10 ** 6
            for i in range(len(firstStartTime)):
                endTime = firstStartTime[i] + firstDuration[i]
                firstEarly = min(firstEarly, endTime)
            ans = 10 ** 6
            for j in range(len(secondStartTime)):
                padding = secondStartTime[j] - firstEarly if secondStartTime[j] > firstEarly else 0
                ans = min(ans, firstEarly + padding + secondDuration[j])

            return ans

        firstValue = earliestTime(landStartTime, landDuration, waterStartTime, waterDuration)
        secondValue = earliestTime(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(firstValue, secondValue)
