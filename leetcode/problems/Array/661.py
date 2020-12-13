'''
Image Smoother
<T> Array

int [][] M 
- gray scale image
- cell is result of average of itself and its neighbors
- if a boundary cell, use only available neighbors



'''
from copy import copy, deepcopy
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        
        neighbors = [[0,0], [0,-1], [0,1], [-1,-1], [-1,0], [-1,1], [1,-1], [1,0], [1,1]]
        
        # its for generating a blank mat with same shape
        ret = deepcopy(M)
        
        for i in range(len(M)):
            for j in range(len(M[i])):
                
                total = 0
                count = 0
                for item in neighbors:
                    x = i + item[0]
                    y = j + item[1]
                    
                    if x<0 or x>=len(M):
                        continue
                    if y<0 or y>=len(M[i]):
                        continue
                    total += M[x][y]
                    count += 1

                #print(M[i][j], total, count)
                ret[i][j] = floor(total/count)
        
        return ret
            
            
        