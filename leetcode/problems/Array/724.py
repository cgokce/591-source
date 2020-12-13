'''
Find Pivot Index
<T> Array

int [] nums
- write method returns pivot index of array
    
    - pivot:
    - index where sum of all numbers to the left of index is equal to sum of all numbers to the right
        - if not exists return -1
        
        - Time O (n) space O(N)


'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        left_sums = []
        total = 0
        
        for item in nums:
            
            left_sums.append(total)
            total += item
            
        #print(left_sums)    
        
        found = -1
        total = 0
        
        for i in range(len(nums)-1, -1, -1):
            item = nums[i]
            #print(total)
            if total == left_sums[i]:
                found = i
            total += item
            
            
            
        return found
            