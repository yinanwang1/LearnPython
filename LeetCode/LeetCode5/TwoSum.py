from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        right = len(nums) - 1

        for left in range(right):
            firstValue = nums[left]
            value = target - firstValue

            while left <= right:
                if nums[right] < value:
                    break
                if nums[right] == value:
                    return [firstValue, nums[right]]
                middle = int((left + right) / 2)
                middleValue = nums[middle]
                if middleValue == value:
                    return [firstValue, middleValue]
                elif middleValue < value:
                    left = middle + 1
                else:
                    right = middle - 1

        return list()



solution = Solution()
solution.twoSum([21,24,33,67,89,102,103,110,127,142,153,160,164,164,169,171,172,204,208,221,224,232,237,242,243,260,262,267,274,275,280,282,320,338,345,349,356,356,362,368,377,392,401,421,465,477,493,502,511,520,528,548,555,559,563,567,570,572,575,584,594,600,603,608,623,646,649,658,675,679,690,698,739,769,779,795,801,803,814,826,830,832,856,872,878,886,890,906,917,925,936,947,948,952,959,961,970,990,996,998],
463)
print("END")