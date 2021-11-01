class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 <= 0:
            return 0

        foundIndex = 0
        foundNums = 0
        tryTimes = 1
        recall = dict()

        while True:
            if tryTimes > n1:
                return foundNums // n2

            for item in s1:
                value = s2[foundIndex]

                if item == value:
                    foundIndex += 1
                    if foundIndex >= len(s2):
                        foundNums += 1
                        foundIndex = 0

            if foundIndex in recall.keys():
                s1cnt_prime, s2cnt_prime = recall[foundIndex]
                pre_loop = (s1cnt_prime, s2cnt_prime)
                in_loop = (tryTimes - s1cnt_prime, foundNums - s2cnt_prime)
                break
            else:
                recall[foundIndex] = (tryTimes, foundNums)

            tryTimes += 1

        times = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
        rest = (n1 - pre_loop[0]) % in_loop[0]
        for i in range(rest):
            for ch in s1:
                if ch == s2[foundIndex]:
                    foundIndex += 1
                    if foundIndex == len(s2):
                        times += 1
                        foundIndex = 0

        return int(times // n2)

solution = Solution()
# result = solution.getMaxRepetitions("acb",
# 4,
# "ab",
# 2)
# result = solution.getMaxRepetitions("bacaba",
# 3,
# "abacab",
# 1)
# result = solution.getMaxRepetitions("baba",
# 11,
# "baab",
# 1)
# result = solution.getMaxRepetitions("acb",
# 1,
# "acb",
# 1)
# result = solution.getMaxRepetitions("lovelive",
# 0,
# "lovelive",
# 10)
# result = solution.getMaxRepetitions("niconiconi",
# 99981,
# "nico",
# 81)
# 预期 7
result = solution.getMaxRepetitions("baba",
11,
"baab",
1)
# 预期 4
# result = solution.getMaxRepetitions("aaa",
# 3,
# "aa",
# 1)
print('END')
print(result)


