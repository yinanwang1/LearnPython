from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if 0 == len(nums):
            return list()

        result = list()
        low = high = 0
        num = nums[0]
        temp = str(num)
        for i in range(1, len(nums)):
            if nums[i] - num > 1:
                if nums[low] != nums[high]:
                    temp += "->" + str(nums[high])
                result.append(temp)
                low = high = i
                temp = str(nums[i])
            else:
                high = i

            num = nums[i]

        if low != high:
            temp += "->" + str(nums[high])

        result.append(temp)


        return result



