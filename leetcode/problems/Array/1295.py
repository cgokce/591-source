'''
Find Numbers with Even Number of Digits
<T> Array


Given arr: nums, return how many contain an even number of digits

- number of digits is log10(x), better use string
- we can just iterate with O(n) and count

'''


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        ret = 0
        
        for item in nums:
            
            #print(item, len(str(item)))
            
            if len(str(item)) % 2 == 0:
                ret += 1
        
        return ret