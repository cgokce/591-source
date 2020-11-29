'''
Count Negative Numbers in a Sorted Matrix
<T> Array

-> int [m][n] grid, sorted reverse order both row wise and col wise
    - Return number of negative numbers in grid


Brute Force Solution
since it is sorted reverse, we can find first positive
- doesn't matter if rows or columns are used


Hint tells using binary search for optimization
- My solution of random search example
- Take random item, if item>0 get another random until?
    -3 -2 -1 [4] 5 6
    -3 -2 -1 

'''

class Solution:
    
    '''Random Search
    # faster but complex logic doesn't worth it, skipping
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        ret = 0
        
        def countNegative(arr):
            size = len(arr)
            # generate random        
            curr = random.randint(0,n)
            if curr > 0:
                ...
        
        for row in grid:
            total = total 
            
    ''' 
    
    #Brute Force
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        ret = 0
        
        for row in grid:
            for item in row:
                if item>=0:
                    continue
                else:
                    ret += 1
        
        return ret