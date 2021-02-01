class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def calc(input: str) -> int:
            chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            total = 0
            for char in chars:
                total += input.count(char)

            return total

        middle = len(s) // 2

        return calc(s[:middle]) == calc(s[middle + 1:])
