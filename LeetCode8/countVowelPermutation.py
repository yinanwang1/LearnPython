# Given an integer n, your task is to count how many strings of length n can be formed under
# the following rules:
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = (
                (dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007, (dp[1] + dp[3]) % 1000000007,
                dp[2] % 1000000007, (dp[2] + dp[3]) % 1000000007,)

        return sum(dp) % 1000000007
