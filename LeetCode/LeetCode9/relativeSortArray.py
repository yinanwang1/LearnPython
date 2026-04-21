
# 给定两个数组，arr1 和 arr2，
#
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。
# 未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rank = {x: i for i, x in enumerate(arr2)}

        def myCmp(x) -> (int, int):
            return (0, rank[x]) if x in rank else (1, x)

        arr1.sort(key=myCmp)

        return arr1


