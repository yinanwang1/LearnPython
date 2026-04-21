import math
from functools import reduce
from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        T = math.ceil(pow(n, 0.5))
        group: dict[int, list] = dict()
        for l, r, k, v in queries:
            if k < T:
                items = group.get(k, [])
                items.append((l,r,v))
                group[k] = items
            else :
                for idx in range(l, r + 1, k):
                    nums[idx] = (nums[idx] * v) % mod
        dif = [1] * (n + T)
        for k, value in group.items():
            dif[:] = [1] * len(dif)
            for l, r, v in value:
                dif[l] = dif[l] * v % mod
                R = r - (r - l) % k + k
                dif[R] = dif[R] * pow(v, -1, mod) % mod
            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % mod
            for i in range(n):
                nums[i] = nums[i] * dif[i] % mod

        return reduce(lambda x, y: x ^ y, nums, 0)


if __name__ == '__main__':
    nums = [1,1,1]
    queries = [[0,2,1,4]]
    solution = Solution()
    result = solution.xorAfterQueries(nums, queries)
    print(result)