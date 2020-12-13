'''
Add to Array-Form of Integer
<T> Array

int x

- given array form of x
    - array of its digits in left to right order
- return the array form of integer X+K


'''
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        num = 0
        order = 1
        for i in range(len(A)-1, -1, -1):
            item = A[i]
            num += order * item
            order *= 10
            
        res = str(num + K)
        ret = []
        
        for c in res:
            ret.append(int(c))
        
        return ret