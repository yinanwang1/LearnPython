from typing import List

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        result = 0
        for i in range(len(A) - 2):
            if A[i] < A[i+1] + A[i+2]:
                result = A[i] + A[i+1] + A[i+2]
                break

        return result



