# https://leetcode.com/problems/employee-importance/

from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates



employees = [Employee(1,5,[2,3]),Employee(2,3,[]),Employee(3,3,[])]
t2 = [Employee(1,2,[5]),Employee(5,-3,[])]



class Solution:
    def getImportanceOld(self, employees: List[List], id: int) -> int:

        importance = 0

        employee_item =  next(filter(lambda employee : employee.id == id, employees))
        importance += employee_item.importance


        for child in employee_item.subordinates:
            child_importance = self.getImportance(employees, child)
            importance += child_importance
        return importance

    def get_importance(self, employees: List[List], id: int) -> int:

        employees_dict = {employee.id: employee for employee in employees}

        def dfs(emp_id):
            employee = employees_dict[emp_id]

            return employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates)

        return dfs(id)
        
sol = Solution()
print(sol.get_importance(employees, 1))