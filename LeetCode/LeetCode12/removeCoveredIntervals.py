from typing import List


# 1288. 删除被覆盖区间
# https://leetcode.cn/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ans = 0
        for i in range(n):
            for j in range(n):
                if i != j and intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    ans += 1
                    break

        return n - ans



if __name__ == '__main__':
    s = Solution()
    print("liahi a " + str(s.removeCoveredIntervals([[1,4],[1,2],[3,4]])))





