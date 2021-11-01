class Solution:
    def compressString(self, S: str) -> str:
        if len(S) <= 2:
            return S

        result = ''
        current_char = ''
        times = 1

        for index in range(len(S)):
            character = S[index]
            if len(current_char) == 0:
                current_char = character
                continue

            if character == current_char:
                times += 1

            if character != current_char:
                result += current_char + str(times)
                current_char = character
                times = 1

            if index == len(S) - 1:
                result += current_char + str(times)

        return result if len(S) > len(result) else S


solution = Solution()
result = solution.compressString("aabcccccaa")
print('end')
print(result)