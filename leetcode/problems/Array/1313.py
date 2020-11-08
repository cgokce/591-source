'''
Decompress Run-Length Encoded List
<T> Array

given: nums, list comprosed with run-length encoding


for each 2 value, we'll generate list
[freq, val]




'''

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        target = []
        
        for i in range(0,len(nums),2):
            
            for j in range(nums[i]):
                target.append(nums[i+1])
            
        
        return target