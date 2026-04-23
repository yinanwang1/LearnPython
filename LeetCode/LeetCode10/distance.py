from collections import Counter, defaultdict
from itertools import accumulate
from typing import List

from torch.nn.modules import distance


# 等值距离和
# https://leetcode.cn/problems/sum-of-distances/description/?envType=daily-question&envId=2026-04-23&status=NOT_STARTED&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJBQ19SQVRFIn1d&difficulty=EASY

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_positions = defaultdict(list)
        for i, num in enumerate(nums):
            num_positions[num].append(i)
        res = [0] * len(nums)
        for positions in num_positions.values():
            total = list(accumulate(positions, initial=0))
            length = len(positions)
            for i, pos in enumerate(positions):
                left = pos * i - total[i]
                right = total[-1] - total[i] - (length - i) * pos
                res[pos] = left + right

        return res




if __name__ == '__main__':
    print(Solution().distance([1,3,1,1,2]))

