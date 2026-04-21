from typing import List

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        content = [0] * 80000

        for x in A:
            content[x] += 1

        ans = taken = 1

        for index in range(80000):
            if content[index] >= 2:
                taken += content[index] - 1
                ans -= (content[index] - 1) * index
            elif taken > 0 and content[index] == 0:
                taken -= 1
                ans += index

        return ans





solution = Solution()
# result = solution.minIncrementForUnique([7,2,7,2,1,4,3,1,4,8])
# result = solution.minIncrementForUnique([1,2,2])
# result = solution.minIncrementForUnique([3,2,1,2,1,7])
# result = solution.minIncrementForUnique([0,2,2])
# result = solution.minIncrementForUnique([2,2,2,2,0])
result = solution.minIncrementForUnique([14,4,5,14,13,14,10,17,2,12,2,14,7,13,14,13,4,16,4,10])
print("END")
print(result)




