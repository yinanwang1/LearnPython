from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeeDic = dict()
        for employee in employees:
            employeeDic[employee.id] = employee

        result = 0
        ids = [id]
        while len(ids) > 0:
            idsTemp = list()
            for id in ids:
                employee = employeeDic[id]
                result += employee.importance
                idsTemp.extend(employee.subordinates)
            ids = idsTemp

        return result