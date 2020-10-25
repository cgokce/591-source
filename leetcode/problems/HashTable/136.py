'''
Single Number
<T> Hash Set

- every element appears twice except for one
- find the single one
- we can use hashmap to count items
- then iterate hashmap again


'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hmap = {}
        
        for item in nums:
            
            if item in hmap:
                hmap[item] += 1
            else:
                hmap[item] = 1
                
        for key in hmap.keys():
            
            if hmap[key] == 1:
                return key
            
        return -1