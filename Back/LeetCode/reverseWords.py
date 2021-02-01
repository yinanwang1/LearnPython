class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        words = words[::-1]
        words = filter(lambda x: len(x) > 0, words)

        return ' '.join(words)