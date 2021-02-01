class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        count = 0

        for num in range(L, R + 1):
            num_bin = bin(num)
            one_count = num_bin.count('1')
            if int(one_count) in primes:
                count += 1

        return count