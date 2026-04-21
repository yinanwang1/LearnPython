from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = list()
        for i in range(1, n+1):
            if 0 == i % 3 and 0 == i % 5:
                result.append("FizzBuzz")
            elif 0 == i % 3:
                result.append("Fizz")
            elif 0 == i % 5:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result
