'''
Positions of Large Groups
<T> Array


string s, lowercase, consequtive groups of same character
    - s = "abbxxxxxzyy" has groups "a", "bb", "xxxxx", "yy"
    - group defined intervals, start and end indices[start,end]
    - LARGE if >=3 characters
    - Return intervals of every large group, sorted by increasing order of start index
    
simple brute force, O(n)
'''

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
                
        inds = []
        count = 0
        prev_ind = -1
        for i in range(len(s)):
            c = s[i]
            
            if i >= len(s)-1:
                if prev_ind != -1:
                    if count >= 2:
                        inds.append([prev_ind,i])
                        prev_ind = -1
                        count = 0
                
            else:
                if s[i] == s[i+1]:
                    count += 1
                    if prev_ind == -1:
                        prev_ind = i
                else:
                    if count >= 2:
                        inds.append([prev_ind,i])
                    prev_ind = -1
                    count = 0
        
        return inds
    
    
                        
                
                
                
                
                
            