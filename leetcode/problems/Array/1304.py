'''
Find N Unique Integers Sum up to Zero
<T> Array
'''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        counter = 0
        ret = []
        
        if n%2==1:
            ret.append(0)
            n -= 1
            
        n = int(n/2)
            
        for i in range(1, n +1):
            ret.append(i)
            ret.append(-1*i)
        
        return ret
        