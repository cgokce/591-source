'''
Array Partition I

given arr-> nums ... 2n integers
    group integers into n pairs of integers makes sum of min(ai, bi) for all i from 1 to n

- we need to sort first
- starting from beginning sum 1, 3....


'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        ret = 0
        i = 0
        
        while (i<len(nums)):
            ret += nums[i]
            i+=2
        
        return ret