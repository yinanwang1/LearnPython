# Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
#
# nums[a] + nums[b] + nums[c] == nums[d], and
# a < b < c < d


from typing import List
from collections import Counter


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        counter = Counter()
        for c in range(n - 2, 1, -1):
            counter[nums[c + 1]] += 1

            for a in range(c):
                for b in range(a + 1, c):
                    ans += counter[nums[a] + nums[b] + nums[c]]

        return ans


def main():
    for i in range(1000, 3000):
        if i % 4 == 0 and i % 100 != 0:
            pass
        else:
            print(i)

    # i = 1900
    # if i % 4 == 0 and i % 100 != 0:
    #     print(i)
    # else:
    #     print("1900 else")



if __name__ == '__main__':
    main()
