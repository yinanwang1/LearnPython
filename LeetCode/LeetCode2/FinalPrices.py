from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        def discount(arr: List[int], num: int):
            for i in arr:
                if i <= num:
                    return num - i
            return num

        for index in range(0, len(prices)):
            value = discount(prices[index+1:], prices[index])
            result.append(value)

        return result

