from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter(nums)

        result = list()
        for key, value in dict(counter).items():
            if value == 1:
                result.append(key)

            if 2 == len(result):
                break

        return result