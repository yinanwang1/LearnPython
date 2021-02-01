class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))

        length = len(a)
        for minus in range(length):
            a_temp = a[minus::]
            print(a_temp)
            if b.count(a_temp) <= 0:
                return len(a_temp)
            a_temp = a[0:(length - minus)]
            print(a_temp)
            if b.count(a_temp) <= 0:
                return len(a_temp)

        return -1

solution = Solution()
result = solution.findLUSlength("aweffwaf", "aweffwaf")
print('END')
print(result)