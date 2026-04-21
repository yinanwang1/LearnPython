from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daySet = set(days)
        duration = [1, 7 , 30]

        def dp(i: int) -> int:
            if i > 365:
                return 0
            elif i in daySet:
                value =  min(dp(i + d) + c for c, d in zip(costs, duration))
                print("111 value is " + str(value))
                return value
            else:
                value = dp(i + 1)
                print("222 value is " + str(value))
                return value

        return dp(1)


solution = Solution()
result = solution.mincostTickets([1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
,[3,13,45])
print('END')
print(result)