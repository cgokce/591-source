'''
Missing Number
<T> Array

int [n] nums, distinct, range[0,n]
    - return only number in range that is missing from array
    
either sort and iterate, seems easiest and fastest
or use a hset to find missing one 
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) >1:
                return nums[i] - 1 
            
        
        if nums[0] == 0:
            return len(nums)
        else:
            return 0