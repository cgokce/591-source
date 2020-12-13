'''
Rank Transform of an Array
<T> Array

int [] arr
- replace each element with its rank

rank represents
    - how large the element is
    - rank is an integer starting from 1
    - larger the element, larger the rank, same elements same rank
    - rank should be small as possible
    

'''

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        arr2 = sorted(arr)
        hmap = {}
        rank = 1
        
        for item in arr2:
            if item not in hmap:
                hmap[item] = rank
                rank += 1
                
        for i in range(len(arr)):
            arr[i] = hmap[arr[i]]
            
        return arr