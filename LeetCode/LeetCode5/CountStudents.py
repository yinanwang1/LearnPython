from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for s in sandwiches:
            like = False
            for _ in range(len(students)):
                if s == students[0]:
                    students.pop(0)
                    like = True
                    break
                else:
                    v = students.pop(0)
                    students.append(v)

            if not like:
                return len(students)

        return 0

