'''
Two Sum
<T> Array <T> HashTable

# Each input have exactly one solution
# There is a one subset total eq == n

# We need only two numbers!!!

# Given [2,7,11,15], target = 9
# 2, 7

'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hmap = {}
        
        for i in range(len(nums)):
            hmap[nums[i]] = i
            
        for i in range(len(nums)):
            remainder = target - nums[i] 
            if remainder in hmap:            
                if i != hmap[remainder]:
                    return [hmap[remainder], i]
        
        
        