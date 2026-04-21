from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIndexs = list()

        for index, num in enumerate(nums):
            if num % 2 != 0:
                oddIndexs.append(index)

        result = 0
        for index, oddIndex in enumerate(oddIndexs):
            if index + k > len(oddIndexs):
                break

            if index - 1 >= 0:
                left = oddIndex - oddIndexs[index - 1] - 1
            else:
                left = oddIndex

            if index + k < len(oddIndexs):
                right = oddIndexs[index + k] - oddIndexs[index + k - 1] - 1
            else:
                right = len(nums) - oddIndexs[index + k - 1] - 1

            result += left * right + 1 + left + right

        return result


solution = Solution()
result = solution.numberOfSubarrays([1,1,2,1,1], 3)
print('END')
print(result)


