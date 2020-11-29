'''
Replace Elements with Greatest Element on Right Side
<T> Array

int [] arr

- replace every element in that array
    - with the greatest among the elements to its right
    - replace the last element with -1
    

sol:
- this is cumulative calculation question
- starting from right, we just cumulatively get max between two elements
- thats the result

'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if not arr:
            return arr

        if len(arr) == 1:
            return [-1]
        
        ptr = len(arr) - 2
        ret = [None for i in range(len(arr))]

        prev_max = -1

        while (ptr >= 0):
            curr_max = max(arr[ptr+1], prev_max)
            ret[ptr] = curr_max
            if curr_max > prev_max:
                prev_max = curr_max

            ptr -= 1
        
        
        ret[-1] = -1
        ret[-2] = arr[-1]
        return ret