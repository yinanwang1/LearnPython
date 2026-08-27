from openpyxl.descriptors import Length


# 2904. 最短且字典序最小的美丽子字符串
# https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/description/

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        ans = s
        left = cnt = 0
        for right, ch in enumerate(s):
            cnt += int(ch)
            while cnt > k or s[left] == "0":
                cnt -= int(s[left])
                left += 1
            if cnt == k:
                t = s[left: right + 1]
                if len(t) < len(ans) or len(t) == len(ans) and t < ans:
                    ans = t
        return ans



if __name__ == '__main__':
    result = Solution().shortestBeautifulSubstring("100011001", 3)
    print("\n\nresult is " + str(result))





