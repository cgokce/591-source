'''
Check Array Formation Through Concatenation
<T> Array

- int [] arr -> unique
- int [][] pieces -> unique

Goal:
- Form arr by concatenating the arrays in pieces in any order
- Not allowed to reorder in each pieces

Return true if it is possible to form the array arr from pieces. 

---

### Simple solution
- Flatten the second array
- Check if they both are equal
    - Though there is one more constraint
    - Subarray values cannot change places
    
Easy way is holding the hashmap for original array to having order memorized
- hmap[item] = position
- Checking position if two consequitive items are fine
total item size n
subarray count m

space O(m)
time O(n + n + c) -> O(n)


- it is seen that items must be continious, that might cause more optimization which i wouldn't chase



'''


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        flatten = []
        hmap = {}
        
        
        for i in range(len(arr)):
            item = arr[i]
            hmap[item] = i
            
        
        #flatten
        for subarr in pieces:
            for i in range(len(subarr)):
                item = subarr[i]
                
                ### Check if item was in original array
                if item not in hmap:
                    return False
                
                ### Check if it is last element, if not check order
                if i < len(subarr)-1:
                    item2 = subarr[i+1]
                    if item2 not in hmap:
                        return False
                    
                    if hmap[item] + 1 != hmap[item2] :
                        return False
        return True
        