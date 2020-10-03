'''
Flipping an Image
<T> Array

- Binary matrix A
    - Flip horizontally
    - Then invert it (Each 0 replaced with 1, 1 replaced with 0, x = 1-x)

Its self explainatory
just do a single pass revert rows while inverting

'''

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(A)):
             
            A[i] = reversed([1 - i  for i in A[i]])
            
        return A
            
            
        