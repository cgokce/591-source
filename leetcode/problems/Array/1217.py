'''
Minimum Cost to Move Chips to The Same Position
<T> Array

int [n] position
- Move all the chips to the same position
- In one step, we can change the position of the ith chip from position[i]


- Need to move all the chips to the same position
- In one step, we can change the position of the ith chip from 
     +2 or -2  with cost:0
     +1 or -1 with cost:1
     
- Return the minimum cost needed to move all the chips to the same position


Sol:

Since -+2 is free, its a matter of classification btw even and odd values
- we need to find the total counts
    - then just get the smallest, since it'll be moved


'''
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = 0
        odds = 0

        for i in range(len(position)):
            if position[i]%2==0:
                evens += 1
            else:
                odds += 1
                
                
        return min(evens,odds)
            
            
            
        