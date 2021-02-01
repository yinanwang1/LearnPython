from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        nums = list(str(n))
        nums.reverse()
        oneNum = 0
        index = 0

        while index < len(nums):
            if nums[index] != '1':
                oneNum += 1 * 10 ** index
            else:
                if index == len(nums) - 1:
                    break
                oneNum += 2 * 10 ** index
                nums[index] = '9'
                indexTemp = index + 1
                while indexTemp < len(nums) - 1:
                    if nums[indexTemp] == '0':
                        nums[indexTemp] = '9'
                        indexTemp += 1
                    else:
                        nums[indexTemp] = str(int(nums[indexTemp]) - 1)
                        break

                if nums[-1] == '0':
                    nums.pop()

            index += 1
            if str(oneNum).count('0') <= 0 and str(n - oneNum).count('0') <= 0:
                break

        return [oneNum, n - oneNum]



