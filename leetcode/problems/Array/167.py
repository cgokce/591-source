'''
Two Sum II - Input Array is Sorted
<T> Array

int [] arr, sorted ascendng

find 2 numbers
    - add up to spesific target numbers
    - return indices of two numbers
    - index1 < index2
    - can't use exact element once
    
we can do two pass
    - Use hash map to have all nums memorized
    - Then for each element, check if complementary using O(1) hmap lookup

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hmap = {}
        
        for i in range(len(numbers)):
            
            item = numbers[i]
            
            if item in hmap:
                hmap[item].append(i)
            else:
                hmap[item] = [i]
                
        
        found = []
        for i in range(len(numbers)):
            
            item = numbers[i]
            
            lookup = target - item
            
            if lookup in hmap:
                for inds in hmap[lookup]:
                    if inds != i:
                        found.append(min(i,inds)+1)
                        found.append(max(i,inds)+1)
                        break
                break
                        
        return found
                        
        