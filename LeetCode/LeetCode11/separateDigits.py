from typing import List

# 2553. 分割数组中数字的数位
# https://leetcode.cn/problems/separate-the-digits-in-an-array/description/


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        response = []
        for num in nums:
            for i in str(num):
                response.append(int(i))

        return response

if __name__ == '__main__':
    print(Solution().separateDigits([13,25,83,77]))
