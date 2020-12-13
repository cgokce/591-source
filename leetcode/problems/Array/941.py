'''
Valid Mountain Array
<T> Array

int [] arr

return true if valid mountain arr
- length >= 3
- i>0 
    - 

'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        switch = False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            
            if not switch:
                if arr[i] > arr[i+1]:
                    if i == 0:
                        return False
                    
                    switch = True 
            else:
                if arr[i] < arr[i+1]:
                    return False

        return switch