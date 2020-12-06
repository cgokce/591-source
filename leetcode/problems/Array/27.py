'''
Remove Element
<T> Array

int [] nums
int val


Remove all instances of that value in-place and return the new length

'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # p is the pos of the pointer
        p = 0
        i = 0
        
        while (i < len(nums)):
            
            if nums[i] == val:
                    i += 1
            else:
                nums[p] = nums[i]    
                i += 1
                p += 1
                
        return p
                
        
# [2]
# 3
