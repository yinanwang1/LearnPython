class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        subTemp = s[::-1]
        if s == subTemp:
            return 1

        return 2







remove = Solution()
result = remove.removePalindromeSub("bbaabaaa")
print(result)