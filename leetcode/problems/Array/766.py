'''
Toeplitz Matrix
<T> Array

int [m][n] matrix

- return true if matrix is Toeplitz
    - if every diagonal from top left to bottom right has the same elements

'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(1, len(matrix), 1):
            toep = matrix[i-1]
            row = matrix[i]
            #print(toep[:-i], row[i:])
            if toep[:-1] != row[1:]:
                return False
        
        return True