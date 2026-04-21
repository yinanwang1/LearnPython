from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_positions: dict[str, list[int]] = {}
        s_keys: List[str] = []
        s_list = list(s)
        t_positions: dict[str, list[int]] = {}
        t_keys: List[str] = []
        t_list = list(t)
        for i in range(len(s)):
            s_char: str = s_list[i]
            try:
                s_pos = s_positions.get(s_char)
                s_pos.append(i)
            except:
                s_positions[s_char] = [i]
                s_keys.append(s_char)

            t_char:str = t_list[i]
            try:
                t_pos = t_positions.get(t_char)
                t_pos.append(i)
            except:
                t_positions[t_char] = [i]
                t_keys.append(t_char)
        for i in range(len(s_keys)):
            s_key = s_keys[i]
            t_key = t_keys[i]
            if s_positions.get(s_key) != t_positions.get(t_key):
                return False

        return True


if __name__ == '__main__':
    s= "12123"
    print(s.split(" "))


