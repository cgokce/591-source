'''
Matrix Diagonal Sum
<T> Array

Return the sum of the matrix diagonals
- Two diagonals
- Discard the common element


can be O(row)
we can do two pointer approach

'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        
        l = 0
        r = len(mat) - 1
        
        ret = 0
        for i in range(len(mat)):
            
            if l != r:
                ret += mat[i][l] + mat[i][r]
            else:
                ret += mat[i][l]
            
            l += 1
            r -= 1
            
        return ret