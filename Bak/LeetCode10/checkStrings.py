






class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_odd = []
        s2_odd = []
        s1_even = []
        s2_even = []
        for index, value in enumerate(s1):
            if index % 2 == 0:
                s1_even.append(value)
                s2_even.append(s2[index])
            else:
                s1_odd.append(value)
                s2_odd.append(s2[index])
        s1_odd.sort()
        s2_odd.sort()
        s1_even.sort()
        s2_even.sort()

        return s1_odd == s2_odd and s1_even == s2_even


if __name__ == '__main__':
    solution = Solution()
    s1 ="abe"
    s2 ="bea"
    print(solution.checkStrings(s1, s2))