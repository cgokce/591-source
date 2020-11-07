'''
Target Array in the Given Order
<T> Array

given: arr<nums> arr<index>

following rules
    - from left to right, read nums[i] and index[i]
    - insert index index[i] the value nums[i] in target array

target array size would be max(index)
since it'll be valid result, len(index) is the same

it is an insert stuff so we need to hold a dif


'''


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        target = []
        
        for i in range(len(index)):
            
            ind = index[i]
            target.insert(ind, nums[i])
            
        return target