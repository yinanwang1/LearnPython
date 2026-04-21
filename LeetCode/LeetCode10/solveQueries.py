from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        value_positions: dict[int, List[int]] = {}
        for i, num in enumerate(nums):
            if num not in value_positions.keys():
                value_positions[num] = [i]
            else:
                value_positions[num].append(i)

        if 1 == len(value_positions.keys()):
            value_positions.items()
            for key, value in value_positions.items():
                if 1 == len(value):
                    return [-1] * len(queries)
            return [1] * len(queries)

        res = []
        nums_length = len(nums)
        for query in queries:
            positions = value_positions.get(nums[query], [])
            if 1 >= len(positions):
                res.append(-1)
                continue
            try:
                index = positions.index(query)
                length = len(positions)
                left = (index - 1 + length) % length
                left_min = query -  positions[left] if query > positions[left] else query + nums_length - positions[left]
                right = (index + 1) % length
                right_min =  positions[right] - query if query < positions[right] else nums_length - query + positions[right]
                res.append(min(left_min, right_min))
            except ValueError:
                res.append(-1)

        return res