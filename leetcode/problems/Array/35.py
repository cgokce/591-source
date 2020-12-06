'''
Search Insert Position
<T> Array

int [] nums, sorted, distinct
int target

Return the index if the target is found
if not return the index where it would be iif it were inserted in order

Simple brute force

'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        found = 0
        
        for i in range(len(nums)):
            
            if nums[i]>=target:
                found = 1
                break
                
        return i + (1-found)
        