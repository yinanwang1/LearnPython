class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = S.split(' ')
        for i, v in enumerate(words):
            if v[0] not in vowel:
                v += v[0]
                v = v[1:]

            v += 'ma' + 'a' * (i + 1)

        return " ".join(words)
