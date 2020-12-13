'''
Minimum Value to Get Positive Step by Step Sum
<T> Array

int [] nums

- start with an initial positive value startValue
    - each iteration: calculate step by step sum of startValue plus elements in nums (l to r)
    - return minimum positive value of startValue such that step by step sum is never less than 1

- Imagine giving a 0, then calculate the minimum step value
    - Add that value as a

'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        
        minsum = 99999
        currsum = 0
        
        
        for item in nums:
            currsum += item
            minsum = min(minsum, currsum)
        
        
        if minsum >= 0:
            return 1
        else:
            return (1 - minsum)
        
        