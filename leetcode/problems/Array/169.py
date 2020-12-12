'''
Majority Element
<T> Array

int [n] arr
- find the majority element
- appears more than n/2 times
    - array is non-empty and the majority element always exist in the array


we can use hmap to count, then iterate that
    - Time: O(n+num_unique_elems), Space: O(num_unique_elems)

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hmap = {}
        
        for item in nums:
            if item in hmap:
                hmap[item] += 1
            else:
                hmap[item] = 1
            
        threshold = len(nums)/2
            
        ret = None
        for k in hmap.keys():
            count = hmap[k]
            if count > threshold:
                ret = k 
                break
                
        return ret
            
        