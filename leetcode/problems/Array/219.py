'''
Contains Duplicate II
<T> Array

int [] arr
int k

- Find if there are two distinct indices i,j
    - absolute difference between i and j is at most k
    
- Another hset question like previous version
    - To find absolute we 


'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hmap = {}
        
        for i in range(len(nums)):
            item = nums[i]
            
            if item in hmap:
                hmap[item].append(i)
            else:
                hmap[item] = [i]
                
        for key in hmap.keys():
            inds = hmap[key]
            #print(inds)
            
            if len(inds) > 1:
                for i in range(1,len(inds)):
                    #print(inds[i-1], inds[i])
                    #print (abs(inds[i-1] - inds[i]), k)
                    if (abs(inds[i-1] - inds[i]) <= k):
                        return True
                    
        
        return False
               
        
                
                
                
                
                
        