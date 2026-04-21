class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        res = ['a'] * (n + m - 1)
        fixed = [False] * (n + m - 1)
        for i, c in enumerate(str1):
            if c == 'T':
                for j, k in enumerate(str2, i):
                    if fixed[j] and k != res[j]:
                        return ""
                    fixed[j], res[j] = True, k
        for i, c in enumerate(str1):
            if c == 'F':
                if any([res[i + j] != str2[j] for j in range(m)]):
                    continue
                for s in range(m - 1, -1, -1):
                    if not fixed[s + i] and res[s + i] == str2[s]:
                        res[s + i] = chr(ord(res[s + i]) + 1)
                        break
                else:
                    return ""
        return ''.join(res)


if __name__ == '__main__':
    str1 = "TFTF"
    str2 = "ab"
    # str1 = "F"
    # str2 = "d"
    # str1 = "TFTF"
    # str2 = "abc"
    solution = Solution()
    result = solution.generateString(str1, str2)
    print(result)
