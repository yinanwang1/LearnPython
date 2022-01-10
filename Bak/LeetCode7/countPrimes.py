# 统计所有小于非负整数 n 的质数的数量。


class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        prime_list = [False] * n
        for i in range(2, n):
            if prime_list[i]:
                continue
            count += 1

            for j in range(i, n, i):
                prime_list[j] = True

        return count


