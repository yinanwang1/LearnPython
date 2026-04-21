from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums

        columns = len(nums[0])
        count = 0
        result = list()
        for _ in range(r):
            values = list()
            for _ in range(c):
                values.append(nums[int(count / columns)][count % columns])
                count += 1

            result.append(values)

        return result

