from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        ans = n

        while left <= right:
            print("left is {}, right is {}".format(left, right))
            mid = ((right - left) // 2) + left
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


solution = Solution()
result = solution.searchInsert([1,3,5,6], 7)
print("result is {}".format(result))



