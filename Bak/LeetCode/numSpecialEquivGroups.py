from typing import List

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        result = list()

        def judgeChar(initial: str, source: str) -> bool:
            if initial == source:
                return True
            initial_list = list(initial)
            initial_even = initial_list[0::2]
            initial_even.sort()
            initial_odd = initial_list[1::2]
            initial_odd.sort()

            source_list = list(source)
            source_even = source_list[0::2]
            source_even.sort()
            source_odd = source_list[1::2]
            source_odd.sort()

            print('initial_even is ' + ''.join(initial_even))
            print('source_even is ' + ''.join(source_even))
            print('initial_odd is ' + ''.join(initial_odd))
            print('source_odd is ' + ''.join(source_odd))


            if ''.join(initial_even) == ''.join(source_even) \
                    and ''.join(initial_odd) == ''.join(source_odd):
                return True

            return False

        while 0 < len(A):
            initial = A[0]
            equiv_list = [initial]
            A_copy = A[1:]
            A.pop(0)

            for character in A_copy:
                print('character is ' + character)
                if judgeChar(initial, character):
                    equiv_list.append(character)
                    A.remove(character)

            result.append(equiv_list)

        print('result is ' + str(result))

        return len(result)


solution = Solution()
result = solution.numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"])
print('End')
print(result)