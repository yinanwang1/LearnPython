


# 3121. 统计特殊字母的数量 II
# https://leetcode.cn/problems/count-the-number-of-special-characters-ii/description/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_dic = dict()
        for i, c in enumerate(word):
            char_list = char_dic.get(c, [])
            char_list.append(i)
            char_dic[c] = char_list
        ans = 0
        keys = list(char_dic.keys())
        keys.sort(reverse=True)
        a_ord, z_ord = ord('a'), ord('z')
        padding = ord('A') - ord('a')
        while 2 <= len(keys):
            key = keys.pop(0)
            key_ord = ord(key)
            if a_ord <= key_ord <= z_ord:
                upper_key = chr(key_ord + padding)
                upper_key_index_list = char_dic.get(upper_key, [])
                if 0 >= len(upper_key_index_list):
                    continue
                keys.remove(upper_key)
                key_index_list = char_dic.get(key, [])
                ans += 1 if max(key_index_list) < min(upper_key_index_list) else 0
            else:
                keys.clear()

        return ans


if __name__ == '__main__':
    print(Solution().numberOfSpecialChars(word="aaAbcBC"))

