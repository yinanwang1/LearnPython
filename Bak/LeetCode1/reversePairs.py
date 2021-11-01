from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def lessNums(num: int, afterNums: List[int]) -> int:
            afterNums.sort()
            numsLength = len(afterNums)

            middle = numsLength // 2
            while True:
                if middle == 0:
                    if num <= afterNums[middle]:
                        return 0
                if middle == numsLength - 1:
                    if num > afterNums[middle]:
                        return numsLength

                if num > afterNums[middle]:
                    if middle + 1 <= numsLength - 1:
                        if num <= afterNums[middle + 1]:
                            return middle + 1

                    middle = (numsLength + middle) // 2
                    continue

                if num <= afterNums[middle]:
                    if middle == 0:
                        return 1

                    middle //= 2
                    continue

        result = 0
        for index, num in enumerate(nums):
            if index > len(nums) - 2:
                break

            resultOne = lessNums(num, nums[(index + 1):])
            result += resultOne

            print('index is ' + str(index))
            print('nums[(index + 1):] is ' + str(nums[(index + 1):]))
            print('resultOne is ' + str(resultOne))

        return result


solution = Solution()
# result = solution.reversePairs([7,5,6,4])
# result = solution.reversePairs([4,5,6,7])
result = solution.reversePairs([1,1,1,1,1])
print("END")
print(result)