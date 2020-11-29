'''
Number of Students Doing Homework at a Given Time
<T> Array

Given two integer arrays
    - startTime<int> []
    - endTİme<int> []

- Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]]



: One solution building a matrix, where each row is a student, column denotes the given time frame
    - We'll fill the rows with students
    - Then just check column
    
: Another solution, easier, just iterate and check if the thing is in between
    - O(n) time, O(1) space, pretty simple since we only need to query one thing


'''

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        
        ret = 0
        
        for i in range(len(startTime)):
            
            s = startTime[i]
            e = endTime[i]
            
            if queryTime >= s and queryTime <= e:
                ret += 1
        
        return ret