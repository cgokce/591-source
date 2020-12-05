'''
Relative Sort Array
<T> Array

int [] arr1
int [] arr2, distinct, subset of arr1


- Sort elements of arr1
    - Relative ordering of items in arr1 are the same in arr2
    - Element don't appear in arr2 should be placed at end of arr1 in ascending order
    
    
Solution, hmap is easier solution here, so we'll use it
'''

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        out_arr = []
        hmap = {}
        
        
        for item in arr1:
            
            if item in hmap:
                hmap[item] += 1
            else:
                hmap[item] = 1
                
                
        
        for item in arr2:
            
            if item in hmap:

                count = hmap.pop(item, None)

                for i in range(count):
                    out_arr.append(item)

                    
        others = []
        for k in hmap.keys():
            count = hmap[k]
            for i in range(count):
                others.append(k)
                
        others = sorted(others)
        out_arr.extend(others)
        
        return out_arr
        
            