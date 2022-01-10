# There is a programming language with only four operations and one variable X:
#
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
#
# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.


from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        v = 0
        for s in operations:
            if s.count("++") > 0:
                v += 1
            else:
                v -= 1

        return v