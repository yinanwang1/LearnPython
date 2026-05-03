

# 796. 旋转字符串
# https://leetcode.cn/problems/rotate-string/description/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        m,n = len(s), len(goal)
        if m != n:
            return False
        for i in range(m):
            for j in range(n):
                if s[(i + j) % m] != goal[j]:
                    break
            else:
                return True
        return False


if __name__ == '__main__':
    print(Solution().rotateString(s = "abcde", goal = "cdeab"))
