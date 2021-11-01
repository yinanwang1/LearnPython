from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greaterDic = dict()
        stackList = list()
        for num in nums2:
            while True:
                if len(stackList) == 0:
                    stackList.append(num)
                    break

                if num < stackList[-1]:
                    stackList.append(num)
                    break
                else:
                    key = stackList.pop()
                    greaterDic[key] = num

        return [greaterDic.get(num, -1) for num in nums1]

