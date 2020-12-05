'''
Make Two Arrays Equal by Reversing Sub-Arrays
<T> Array

Given
- int [] target
- int [] arr
arrays are equal length


1 step: select any non-empty-sub-array of arr and reverse it
    - can do multiple steps
Return true if you can make arr equal to target



----

Solution close to O(n)

Case1: 
- If one subarr is reverse, it is easy to catch it, when difference, use a something like a stack to match those, until same line comes
abcdef
abdcef
Case2:
- Two subarrays nested

    - First small then large
    
    ab[cd]ef
    a[bdce]f
    a ecdb f  -> not in place e , needs to 2*k items after it until the next unmatch
              -> not in place f , needs to swap with first item, and should match
    
    a ebdc f
    
    
- For a given interval, per 2 item
    - we can do either simple collect
    - or reverse collect

- Rather we can also get other matches
    - It renders interval detection useless
    

It is getting unnecessarily complex
FAIL. We can repeatedly swap between two to get any results
- It results in just checking if two arrays have same items or not
---- 

Easier solution then:

    abcdef
    abdfec?
    
Since we are allowed infinite reverse
    
we can just sort both , check equality
- it'll make sure both have same items



'''

class Solution:
    
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        return sorted(arr) == sorted(target)
        
    
    '''
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        
        intervalStart = None
        intervalSize = None
        
        for i in range(len(arr)):
            item1 = arr[i]
            item2 = arr[i]
        
            if item1 != item2:
                if intervalStart == None:
                    intervalStart = i
                    intervalSize = 1
                else:
                    intervalSize += 1
            else:
                skippedInterval = True
     '''         
            
                    
            
            
            
                
            
            
            
        
        