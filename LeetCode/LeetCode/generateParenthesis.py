from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.processing = dict()

        def recursion(num: int) -> set:
            if 1 == num:
                return {'()'}

            if num in self.processing.keys():
                return self.processing[num]

            temp_set = set()
            for index in range(1, num):
                left = recursion(index)
                right = recursion(num - index)

                for item1 in left:
                    for item2 in right:
                        half = len(item1) // 2
                        item3 = item1[:half] + item2 + item1[half:]

                        temp_set.add(item1 + item2)
                        temp_set.add(item3)

                        print('item1 is ' + item1)
                        print('item2 is ' + item2)
                        print('item3 is ' + item3)
                        print('temp_set is ' + str(temp_set))
            self.processing[num] = temp_set

            return temp_set

        return list(recursion(n))



solution = Solution()
result = solution.generateParenthesis(4)
# result = solution.generateParenthesis(2)
# result = solution.generateParenthesis(3)
print('END')
print(result)




