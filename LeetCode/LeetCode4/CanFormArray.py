from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = 0

        while index < len(arr):
            value = arr[index]
            tempIndex = index
            for array in pieces:
                if value == array[0]:
                    for i in range(1, len(array)):
                        index += 1
                        if index >= len(arr):
                            return False
                        if arr[index] == array[i]:
                            continue
                        else:
                            return False
                    pieces.remove(array)
                    index += 1
                    break
            if tempIndex == index:
                return False

        return True

