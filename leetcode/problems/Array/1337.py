'''
The K Weakest Rows in a Matrix
<T> Array

int [m][n] mat
    - 1 representing soldiers
    - 0 represent civilians
    
- return indexes of the k weakest rows in the matrix
    - weaker = less soldiers


'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        row_str = []
        
        for i in range(len(mat)):
            row = mat[i]
            row_str.append([sum(row),i])
            
        
        
        row_str = sorted(row_str, key=lambda x:x[0])
        row_str = [a[1] for a in row_str]
        return row_str[:k]