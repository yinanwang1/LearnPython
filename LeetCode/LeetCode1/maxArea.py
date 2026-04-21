from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxValue = 0

        while left < right:
            maxValue = max(maxValue, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxValue




solution = Solution()
result = solution.maxArea([1,8,6,2,5,4,8,3,7])
print('END')
print(result)




