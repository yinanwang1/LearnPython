from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            if i % 2 == 0 and A[i] % 2 == 0:
                continue
            elif i % 2 == 1 and A[i] % 2 == 1:
                continue
            elif i % 2 == 0:
                for j in range(i + 1, len(A)):
                    if A[j] % 2 == 0:
                        temp = A[i]
                        A[i] = A[j]
                        A[j] = temp
                        break
            else:
                for j in range(i + 1, len(A)):
                    if A[j] % 2 == 1:
                        temp = A[i]
                        A[i] = A[j]
                        A[j] = temp
                        break

        return A