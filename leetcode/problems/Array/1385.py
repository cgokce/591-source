'''
Find the Distance Value Between Two Arrays
<T> Array

int [] arr1
int [] arr2
int d

return distance btw two arrays
    - distance value: 
        - num elements arr[i] such that
        - there is no any element arr2[j]
        - where |arr1[i] - arr2[j]| > d


Failed:
- we only need the min and the max values in arr2
    - later traverse each item in arr1 to find the correspondances

Since we want similar values
- there seems like no smart approach here, just doint O(n*m) way nested


'''

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        ret = 0
        for item1 in arr1:
            flag = True
            
            for item2 in arr2:
            
                if ( abs(item1 - item2) <= d ):
                    flag = False
        
            if (flag):
                ret += 1
                
        return ret
        
    
    '''
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        if not arr2:
            return len(arr1)
        
        
        minVal = arr2[0]
        maxVal = arr2[0]
        
        for item in arr2:
            minVal = min(item, minVal)
            maxVal = max(item, maxVal)
        
        ret = 0
        for item in arr1:
            
            if ( abs(item - minVal) > d ) and ( abs(item - maxVal) > d):
                ret += 1
        
        return ret
    '''
        