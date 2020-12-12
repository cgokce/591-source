'''
Contains Duplicate
<T> Array

int [] arr
- Find if it contains duplicates
- Return true if any value appears at least twice, else return false

its a hash set question

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hset = set()
        for item in nums:
            if item in hset:
                return True
            else:
                hset.add(item)
        
        return False
            