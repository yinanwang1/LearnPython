from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        index = 0
        result = list()
        for num in range(1, n + 1):
            if index >= len(target):
                break
            if num == target[index]:
                index += 1
                result.append('Push')
                continue
            result.append('Push')
            result.append('Pop')

        return result



