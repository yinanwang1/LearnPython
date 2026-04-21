class Solution:
    def maxDepth(self, s: str) -> int:
        nums = 0
        maxNums = 0
        for char in s:
            if char == '(':
                nums += 1
                maxNums = max(nums, maxNums)
            elif char == ')':
                nums -= 1
        
        return maxNums