from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = list()
        for i in range(len(nums)):
            while i + 1 != nums[i]:
                print(i)
                print(nums)
                if nums[nums[i] - 1] == nums[i]:
                    result.append(i + 1)
                    break
                index = nums[i] - 1
                temp = nums[index]
                nums[index] = index + 1
                nums[i] = temp

        resultTemp = list()
        for i in result:
            if i + 1 != nums[i]:
                resultTemp.append(i + 1)

        return resultTemp


''.translate()





