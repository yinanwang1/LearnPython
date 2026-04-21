class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        def filterNumA(x) -> bool:
            value = ord(x)
            return 48 <= value <= 57 or 65 <= value <= 90 or 97 <= value <= 122

        values = list(filter(filterNumA, s))
        half = len(values) // 2
        firstHalf = "".join(values[:half])
        lastHalf = "".join(values[::-1][:half])
        return firstHalf.lower() == lastHalf.lower()

