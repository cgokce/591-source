'''
Lucky Numbers in a Matrix
<T> Array

int [m][n] numbers, distict

- Return all lucky numbers any order
- Lucky number:
    - Minimum element in its row and maximum element in its column
    
    
-- Brute Force 
Just check , O(n *n*m)?


-- Sol2 
- We can calculate minimum of rows
- Max of cols
- Then return the matching elems
- Similar to O(n*m) - 2*n*m + n + m
- Easier calculation trick is having whole matrix again for mins and maxes

'''

class Solution:
    
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        # Find the max of the rows
        
        min_rows = []
        
        for row in matrix:
            min_rows.append( min(row))
        
        print(min_rows)
        
        # Find the man of cols
        # Transpose matrix, do the same
        
        transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 
        
        max_cols = []
        found = []
        
        for col in transposed:
            item = max(col)
            max_cols.append(item)
            if item in min_rows:
                found.append(item)
        
        print(max_cols)
        
        # Match max
        return found
    
    '''
        ### Calculate the max cols
        cols_max = []
        
        for r in range(len(matrix)):
            biggest = -1
            for c in range(len(matrix[r])):
                
                biggest = max(biggest, matrix[r][c])
            
            cols_max.append(biggest)
            
        for r in range()
            
    '''