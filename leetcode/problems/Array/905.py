'''
Sort Array By Parity
<T> Array

Given:
unsigned int [] A

Const:
- Return array consisting all the even elems of A
- Followed by all the odd elements of A
- Return any answer array satisfies condition

Solution:
- Straight brute force O(n) time
- will use O(n) space to hold the evens and odds
    - Swap would be no space constraint, thats another days job

- Another alternative is using two pointers for final array, though this is simpler to understand

'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        evens = []
        odds = []
        
        for item in A:

            if item %2 == 0:
                evens.append(item)
            else:
                odds.append(item)
        
        # evens.extend(odds)
        return evens + odds 
        
        