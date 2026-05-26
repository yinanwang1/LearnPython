
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        result = set()
        padding = ord('a') - ord('A')
        for i in range(n):
            ch = word[i]
            ch_ord = ord(word[i])
            for j in range(1, n):
                if abs(ch_ord - ord(word[j])) == padding:
                    result.add(ch.lower())

        return len(result)


if __name__ == '__main__':
    print(Solution().numberOfSpecialChars(word="aaAbcBC"))
