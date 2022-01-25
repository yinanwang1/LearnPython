# There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer.
# A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing
# to the character 'a'.
# Each second, you may perform one of the following operations:
# Move the pointer one character counterclockwise or clockwise.
# Type the character the pointer is currently on.
# Given a string word, return the minimum number of seconds to type out the characters in word.

class Solution:
    def minTimeToType(self, word: str) -> int:
        char, step = 'a', 0
        for c in word:
            distance = abs(ord(char) - ord(c))
            step += min(distance, 26 - distance)
            step += 1
            char = c

        return step
