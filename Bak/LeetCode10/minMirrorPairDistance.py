from typing import List

from streamlit.elements import empty


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        pre_dict = {}
        res = len(nums)
        for i, num in enumerate(nums):
            if num in pre_dict:
                res = min(res, i - pre_dict[num])
            pre_dict[int(str(num)[::-1])] = i
        return res if res < len(nums) else -1





if __name__ == '__main__':
    print(Solution().minMirrorPairDistance([1, 2, 3, 4, 5]))
    # print(Solution().minMirrorPairDistance([9,9]))
