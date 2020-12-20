'''
Monotonic Array
<T> Array

int [] A

- Monotonic if
    - All monotone increasing or monotone decreasing
    

'''
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        if len(A) == 1 or not A:
            return True
        
        rising = -1
        
        for i in range(len(A)-1):
            
            # increasing
            if A[i+1] > A[i]:
                if rising == -1:
                    rising = 1
                elif not rising:
                    return False
            elif A[i] > A[i+1]:
                if rising == -1:
                    rising = 0
                elif rising:
                    return False
                
        return True
        
        
                    