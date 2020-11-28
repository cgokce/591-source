'''
Given n,m: dimensions of matrix
    - initialized by zeros
Given indices: array
    - indices[i] = [ri, ci]

Aim:
    - For each pair ri, ci you have to increment all cells in row ri and column ci by 1.
    - Return the number of cells with odd values in the matrix after applying increment
    
Return number of cells with odd values in the matrix after applying the increment to all indices

---

Simple approach would be to aggregate
Since ri and ci is kind of unrelated, we can group data
hashmap?
- Then apply the brute force solution
- No need to hold matrix since we have our hmaps

'''

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        
        rowmap = {}
        colmap = {}
        
        for item in indices:
            
            r = item[0]
            c = item[1]
            #print(r,c)
            
            if r in rowmap:
                rowmap[r] += 1
            else:
                rowmap[r] = 1
                
            if c in colmap:
                colmap[c] += 1
            else:
                colmap[c] = 1
                
                
        to_ret = 0
        for r in range(n):
            for c in range(m):
            
                val = 0
                if r in rowmap:
                    val += rowmap[r]
                if c in colmap:
                    val += colmap[c]
                    
                #print(val)
            
                if val %2 == 1:
                    to_ret += 1
            
        return to_ret