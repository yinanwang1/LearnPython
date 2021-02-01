from typing import List

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        def binarySearch(mountain, target, l, r, key=lambda x: x) -> int:
            target = key(target)

            while l <= r:
                middle = (l + r) // 2
                cur = key(mountain.get(middle))

                if cur == target:
                    return middle
                elif cur < target:
                    l = middle + 1
                else:
                    r = middle - 1

            return -1


        l, r = 0, mountain_arr.length() - 1

        while l < r:
            middle = (l + r) // 2

            if mountain_arr.get(middle) < mountain_arr.get(middle + 1):
                l = middle + 1
            else:
                r = middle - 1

        mountainTop = l
        print('mountainTop is ' + str(mountainTop))

        index = binarySearch(mountain_arr, target, 0, mountainTop)
        if index != -1:
            return index

        return binarySearch(mountain_arr, target, mountainTop, mountain_arr.length() - 1, key=lambda x: -x)























