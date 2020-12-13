'''
Maximum Average Subarray I
<T> Array

int [n] arr

- find contigious subarray 
- length k
- maximum average value, return that


bad solution
- use n sliding windows, its unnecessary

another brute force easier to implement
- for all subarrays,[0: n], [1:n]...
    - get prefix sums/averages
- Gives the time limit for bigger inputs


better idea:
Since we know the lenght, we just use sliding window with given length
    O(nk)
    - TIME LIMIT STILL
- Be optimized by plus/minus one at every step
    - THIS ONE WORKS +
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        if not nums:
            return 0.0
        elif len(nums)==1:
            return nums[0]/1
    
        ind = 0    
        total = 0
        for j in range(k):
            total += nums[j]
        
        maxAvg = total/k
        
        for i in range(len(nums)-k):
            # remove i, add k
            total = total - nums[i] + nums[i+k]
            maxAvg = max(maxAvg, total/k)
        
        return maxAvg
            

    '''
    # All lengths, time limit
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if not nums:
            return 0.0
        elif len(nums)==1:
            return nums[0]/1
        
        
        maxAvg = -1
        
        for i in range(len(nums)):
            
            subarr = nums[i:len(nums)].copy()
            
            total = 0
            for j in range(len(subarr)):
                item = subarr[j]
                total += item
                avg = total/(j+1)
                if (j+1) == k:
                    maxAvg = max(maxAvg, avg)
                
        return maxAvg
    '''