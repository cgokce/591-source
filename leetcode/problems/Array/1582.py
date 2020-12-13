'''
Special Positions in a Binary Matrix
<T> Array

int [rows][cols] mat
    - either 0 or 1
    
return number of special positions
    - pos i,j is special if i,j = 1
    - and all other elems in row i,j are 0

'''
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
           
        colSum = []
        transposed = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
        
        for col in transposed:
            colSum.append(sum(col))
            
        count = 0
        for i in range(len(mat)):
            row = mat[i]
            if sum(row) == 1:
                for j in range(len(mat[i])):
                    if mat[i][j] == 1 and colSum[j] == 1:
                        count += 1
                    
        return count
            
        
        