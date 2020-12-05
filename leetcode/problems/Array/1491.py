'''
Average Salary Excluding the Minimum and Maximum Salary
<T> Array

int [] salary
    - unique elems
    - employee salaries
- Return the average salary of employees excluding the minimum and maximum salary


'''

class Solution:
    def average(self, salary: List[int]) -> float:
        
        return (sum(salary) - min(salary) - max(salary)) / max(1,len(salary)-2)
        