
# https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.

"""

from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List[List], id: int) -> int:

        employee_dict = {emp.id: emp for emp in employees}

        def dfs(emp_id):
            employee =  employee_dict[emp_id]
            emp_importance = employee.importance

            for sub_id in employee.subordinates:
                emp_importance = emp_importance + dfs(sub_id)

            return emp_importance

        importance = dfs(id)
        return importance
    

if __name__ == "__main__":
    # Create Employee objects from input [[1,5,[2,3]],[2,3,[]],[3,3,[]]]
    employees = [
        Employee(id=1, importance=5, subordinates=[2, 3]),
        Employee(id=2, importance=3, subordinates=[]),
        Employee(id=3, importance=3, subordinates=[])
    ]

    # Test with id = 1
    solution = Solution()
    result = solution.getImportance(employees, id=1)
    print(result)