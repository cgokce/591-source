'''
Duplicate Zeros
<T> Array

int [] arr

- duplicate each occurance of zero
    - shifting remaining elems to the right
    - elements beyond the length of the array are not written
    - in place

'''

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        total = len(arr)
        i = 0
        
        while (i<total):
            
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i+=1
            i+=1
            
        return