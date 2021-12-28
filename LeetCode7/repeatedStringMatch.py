# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.
#
# Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        try:
            i = b.index(a)
        except ValueError:
            try:
                a.index(b)
                return 1
            except ValueError:
                try:
                    (a + a).index(b)
                    return 2
                except ValueError:
                    return -1
        l = len(a)
        if i > l or a[l - i:] != b[:i]:
            return -1
        count = 1 if i == 0 else 2
        i += l
        while i <= len(b):
            if b[i: i + l] == a:
                count += 1
                i += l
            else:
                break

        if i == len(b):
            return count
        if b[i:] == a[:len(b) - i]:
            return count + 1
        else:
            return -1



