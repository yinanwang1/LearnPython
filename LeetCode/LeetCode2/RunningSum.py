from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tempNums = []
        for num in nums:
            if 0 == len(tempNums):
                tempNums.append(num)
            else:
                tempNums.append(tempNums[-1] + num)

        return tempNums
