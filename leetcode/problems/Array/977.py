'''
Squares of a Sorted Array
<T> Array

Given: int[] A, sorted in increasing order
- Return array of the squares of each number
- Also sorted in increasing order


Ranges are small
- so simple brute force is viable
- Get squares and sort O(nlogn)

- A bit optimized, two pointers solution
    - Find the position of smallest positive integer
    - Two pointers, that increasingly add squared results to final array according to absolute value
    - Still bit complex, skipping this

- Much better approach 
    - Two pointers starting from each end
    - We instead try to converge into descending list, which will later reversed
    - O(n)

'''

class Solution:
    
    # Two Pointers
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        p1 = 0
        p2 = len(A)-1
        ret = []
        
        while p1 <= p2:
            
            item1 = A[p1]
            item2 = A[p2]
            
            if abs(item1) <= abs(item2):
                ret.append(item2*item2)
                p2 -= 1
            else:
                ret.append(item1*item1)
                p1 += 1
    
        ret.reverse()
        return ret
    
    
    '''
    # Brute Force
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        ret = []
        
        for item in A:
            ret.append(item*item)
        
        return sorted(ret)
     ''' 
        