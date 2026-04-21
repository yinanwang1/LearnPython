class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1_list, s2_list = list(s1), list(s2)

        if s2_list == s1_list:
            return True
        temp = s1_list.copy()
        temp[1], temp[3] = temp[3], temp[1]
        if s2_list == temp:
            return True
        temp = s1_list.copy()
        temp[0], temp[2] = temp[2], temp[0]
        if s2_list == temp:
            return True
        temp[1], temp[3] = temp[3], temp[1]
        if s2_list == temp:
            return True

        return False