'''
Most Visited Sector in a Circular Track
<T> Array

int n
int [] rounds

- Circular tracks n sectors [1,n]
- Marathon will be held on this track
    - m rounds
    - i-th round starts at sector rounds[i-1], ends rounds[i] ()
    - round 1 starts at sector rounds[0] ends at sector rounds[1]
    - it says ccw, but its irrelevant
    - return most visited sectors in ascending order
    
    
- Brute force, still we dont need to count a lap, since a lap traverses all sectors at once
    - So, get rid of laps, then count visits x to y
    - Easier just first to end
    
'''

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        most = []
        i = rounds[0]
        while i != rounds[-1]:
            most.append(i)
            if i == n:
                i = 1
            else:
                i += 1
            
        most.append(i)
        most.sort()
        return most