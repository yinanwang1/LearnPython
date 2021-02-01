class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        memo = {}

        def recursion(eggs: int, floor: int) -> int:
            print('eges is ' + str(eggs) + " floor is " + str(floor))

            if (eggs, floor) in memo:
                return memo[eggs, floor]

            if eggs == 1:
                ans = floor
            elif floor == 0:
                ans = 0
            else:
                ans = 1 + min(max(recursion(eggs - 1, x - 1), recursion(eggs, floor - x))
                              for x in range(1, floor + 1))

            memo[eggs, floor] = ans

            return ans

        return recursion(K, N)


solution = Solution()
# result = solution.superEggDrop(1, 2)
# result = solution.superEggDrop(2, 6)
result = solution.superEggDrop(3, 14)
# result = solution.superEggDrop(1, 3) # 3
# result = solution.superEggDrop(2, 1) # 1
# result = solution.superEggDrop(1, 1) # 1
# result = solution.superEggDrop(2, 2) # 2
print('END')
print(result)
