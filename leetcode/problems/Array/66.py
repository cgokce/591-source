'''
Plus One
<T> Array

int [] array, not empty
    - corresponds to decimal digits represnting a non-negative integer


- Bad question, what happens when 9 comes?
- Testing input

Input
[9]
Output
[1,0]

Simple solution, just conversion
arr -> string -> int -> plus one -> array

Another brute force solution
- Reverse traverse array, go with adding 1s
- Will insert at position if overflows

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        for i in range(len(digits)-1, -1, -1):
            
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
            else:
                digits[i] += 1
                break
                
        return digits