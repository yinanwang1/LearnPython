from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        desc = True
        positive = 0
        negative = 0
        for i in range(0, len(A) - 1):
            minus = A[i + 1] - A[i]
            if minus == 0:
                print("1")
                return False
            elif minus > 0:
                positive += 1
                if desc is False:
                    print("2")
                    return False
            else:
                negative += 1
                if desc is True:
                    desc = False
        print("positive is {}, negative is {}".format(positive, negative))
        return positive > 0 and negative > 0



