'''
Count Number of Teams
<T> Array

-> 3 items
-> Choose 3 soldiers amongst them i<j<k under following rules
    ->  r1 < r2 < r3  or r1 > r2 > r3

return all number of teams

---------------

n <= 200, so brute force is possible

time O(n^3) space O(1)
check all combinations, add the team if conditions met



'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        
        ret = 0
        
        for i in range(len(rating)):
            
            for j in range(i, len(rating)):
                
                for k in range(j, len(rating)):
                    
                    if (rating[i] < rating[j] and rating[j] < rating[k]) or (rating[i] > rating[j] and rating[j] > rating[k]):
                        ret += 1
                        
        return ret