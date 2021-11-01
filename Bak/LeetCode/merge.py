from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        def dealwith(inputNums: List[List[int]]) -> List[List[int]]:
            nums = list()

            for num in inputNums:
                nums += num

            result = list()
            index = 0

            while index < len(nums) - 1:
                temp = [nums[index]]
                if index + 3 > len(nums):
                    temp.append(nums[index + 1])

                    result.append(temp)
                    break

                num1 = nums[index + 1]
                num2 = nums[index + 2]

                if num1 >= num2:
                    temp.append(max(num1, nums[index + 3]))

                    index += 4
                else:
                    temp.append(num1)
                    index += 2

                result.append(temp)

            return result

        middle = dealwith(intervals)
        print(middle)

        while True:
            middleTemp = dealwith(middle)
            print(middleTemp)
            if len(middle) == len(middleTemp):
                break
            else:
                middle = middleTemp

        return middle



