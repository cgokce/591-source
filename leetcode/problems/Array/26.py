'''
Remove Duplicates From Sorted Array
<T> Array

int [] nums, sorted
    - remove duplicates in-place 
    - each element appear only once and returns the new length
    
- Do not allocate extra space for another array, must be O(1)

- Bad question


 1 2 3 3 3 4 4 5 6 7 7 8 8 8 9 10
 
 p p p p p p 
             i i
             p
             5
 


'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Current write pointer
        p = 0
        i = 0
        
        while i < len(nums):
            
            #print(i,p)
            nums[p] = nums[i]
            
            if i == len(nums)-1:
                break
            else:
                # Start of the repeat cycle
                if nums[i] == nums[i+1]:
                    
                    while nums[i] == nums[i+1]:
                        if i+1 == len(nums)-1:
                            p -= 1
                            break
                        i += 1 
                i += 1
            p += 1
               
        return p+1
    
# [1,1]
# [1,2]