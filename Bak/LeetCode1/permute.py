from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recycle(childNums: List[int]) -> List[List[int]]:
            if 1 == len(childNums):
                return [childNums]

            print('childNums is ' + str(childNums))

            arrayList = list()
            for index, num in enumerate(childNums):
                childNumsTemp = childNums.copy()
                childNumsTemp.remove(num)
                childList = recycle(childNumsTemp)

                for numList in childList:
                    resultList = [num]
                    resultList.extend(numList)

                    print('resultList is ' + str(resultList))

                    arrayList.append(resultList)

            print("arrayList is " + str(arrayList))

            return arrayList

        return recycle(nums)


solution = Solution()
result = solution.permute([1,2,3])
print("END")
print(result)