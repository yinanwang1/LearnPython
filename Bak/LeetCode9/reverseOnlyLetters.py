
# Given a string s, reverse the string according to the following rules:
#
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right, temp = 0, len(s) - 1, list(s)
        while left < right:
            l, r = temp[left], temp[right]
            if not ('a' <= l.lower() <= 'z'):
                left += 1
                continue
            if not ('a' <= r.lower() <= 'z'):
                right -= 1
                continue

            l.isalpha()

            temp[right], temp[left] = l, r
            left += 1
            right -= 1

        return "".join(temp)



