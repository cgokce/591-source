'''
Sort Array By Parity II
<T> Array

unsigned int [] A 
    - half odd, half even

- Sort the array so that whenever A[i] is odd, i is odd and whenever A[i] is even
    - You may return any answer array that satsifies this condition

E O E O 

'''

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        evens = []
        odds = []
        final = []
        
        
        for item in A:
            
            if item%2==0:
                evens.append(item)
            else:
                odds.append(item)
                
        
            while len(evens) >0 and len(odds) > 0:
                final.append(evens.pop())
                final.append(odds.pop())
        
        return final