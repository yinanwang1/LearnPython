from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = len(nums) * 3
        key_position: dict[int, list[int]] = {}
        for index, num in enumerate(nums):
            positions = key_position.get(num, [])
            positions.append(index)
            key_position[num] = positions
        for key, positions in key_position.items():
            if 3 > len(positions):
                continue
            for i in range(len(positions) - 2):
                res = min(res, abs(positions[i] - positions[i + 1]) + abs(positions[i + 1] - positions[i + 2]) + abs(positions[i] - positions[i + 2]))

        return -1 if len(nums) * 3 == res else res

