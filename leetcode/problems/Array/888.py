'''
Fair Candy Swap
<T> Array

Alice Bob have candy barrs

int [] A
int [] B
    - size of the ith bar of candy


- Exchange 1 candy bar each. 
    - They both have same total amount of candy

- Return integer array
    - ans[0] size of candy bar Alice exchange
    - ans[1] size of the candy bar Bob exchange

There is brute force solution
    - Get sum of all
    - Then look for O(n^2) if satisfy the cond
    - GIVES TIME LIMIT ERR
    
SET Solution!
    - Generate set from A
    - Then iterate B (O(n))
    - Search the matching item using O(1) lookup from A's set
    

'''

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
        diff = sum(B) - sum(A)
        hset = set(A)
        
        for item in B:
            lookup = item - int(diff/2)
            if lookup in hset:
                return [lookup, item]
            
        return []
        
        
    '''
    # Brute Force gives time limit
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
        diff = sum(A) - sum(B)
        
        for item1 in A:
            for item2 in B:
                
                if (2 * (item1 - item2)) == diff:
                    return [item1, item2]
        
        return []
    '''             
        