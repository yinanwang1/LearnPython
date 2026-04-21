# class Solution:
#     def waysToChange(self, n: int) -> int:
#         if 0 == n:
#             return 0
#
#         i = n // 25
#         j = (n % 25) // 10
#         k = (n % 25 % 10) // 5
#         l = (n % 25 % 10) % 5
#
#         print(i)
#         print(j)
#         print(k)
#         print(l)
#
#         print("r-value")
#         result = 0
#         if l > 0:
#             result = 1
#         print(result)
#
#         if result > 0:
#             if k > 0:
#                 result *= k * 2
#         else:
#             result = k * 2
#         print(result)
#
#         if result > 0:
#             if j > 0:
#                 result = result * j * 3 + 1
#         else:
#             result = j * 4
#         print(result)
#
#         if result > 0:
#             if i > 0:
#                 result = result * i * 12 + 1
#         else:
#             result = i * 13
#         print(result)
#
#         return result % 1000000007


class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7

        ans = 0
        for i in range(n // 25 + 1):
            rest = n - i * 25
            a, b = rest // 10, rest % 10 // 5
            ans += (a + 1) * (a + b + 1)
        return ans % mod


solution = Solution()
# result = solution.waysToChange(25)
result = solution.waysToChange(61)  # 73
print('END')
print(result)