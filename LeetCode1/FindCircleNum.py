from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        nums = list()

        def updateStatus(i: int, j: int):
            exist = False
            existIndex = list()
            for index, value in enumerate(nums):
                if i in value or j in value:
                    if exist:
                        existIndex.append(index)
                        continue
                    exist = True
                    value.add(i)
                    value.add(j)
                    existIndex.append(index)

            if not exist:
                nums.append({i, j})
            elif 1 < len(existIndex):
                existIndex.sort(reverse=True)
                result = set()
                for k in existIndex:
                    result = set.union(result, nums[k])
                    nums.pop(k)
                nums.append(result)

        for i in range(n):
            for j in range(i, n):
                if 1 == isConnected[i][j]:
                    updateStatus(i, j)

        return len(nums)



