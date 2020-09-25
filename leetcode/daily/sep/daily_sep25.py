'''
Largest Number
<T> Sort

Given a list of non negative integers
Arrange them such that they form the largest number

-> Return a string


- Each number is a value forming individual digits
Bad idea:
- We can use multiple sorts
    Sort by 1st elem
    Sort by second elem
    Third elem and so on,

Better:
-> Using the LC provided solution algorithm
Solution builds on writing a custom sort operation
We need to check [a b] > [b a] 
[] denotes concat

So first convert them to string
second build a greater() function for comparison
    -> I'd skip operator overload for simplicity

'''

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(a , b):
            if (str(a) + str(b) > str(b) + str(a)):
                return -1
            else:
                return 1
            
        
        arr = sorted(nums, key=cmp_to_key(compare))
        
        if arr[0] == 0:
            return "0"
        else:
            return "".join([str(i) for i in arr])
        
        
            
        