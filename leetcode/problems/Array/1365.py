'''
How many numbers are smaller than the current number

given: arr<nums> 

for each nums[i] how many numbers in array are smaller than it

it is easy we need to sort
use hmap for counts
then print the location of item in sorted array using the predefined hmap


'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ordered = sorted(nums)
        hmap = {}
        
        for i in range(len(ordered)):
            item = ordered[i]
            if item not in hmap:
                hmap[item] = i
        
        ret = [None for i in range(len(nums))]
        
        for i in range(len(nums)):
            item = nums[i]
            ret[i] = hmap[item]
        
        return ret