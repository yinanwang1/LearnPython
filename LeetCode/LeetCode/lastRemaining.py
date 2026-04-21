class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))
        index = 0

        while len(nums) > 1:
            remain = len(nums) if m % len(nums) == 0 else m % len(nums)
            index += remain - 1

            if index >= len(nums):
                index -= len(nums)

            print(nums)
            print(index)

            nums.pop(index)

            if index >= len(nums):
                index = 0

        return nums[0]







solution = Solution()
# result = solution.lastRemaining(5, 1)
# result = solution.lastRemaining(5, 3)
result = solution.lastRemaining(10, 17)
# result = solution.lastRemaining(88, 10)
print('END')
print(result)