'''
Can Make Arithmetic Progression From Sequence
<T> Array

- int [] arr
- arithmetic progression: Sequence of numbers 
    - difference between any two consecutive elements is the same
- Return true if the array can be rearranged to form an artihmetic progression

135 diff 2
531 diff -2


-----

Sol:

a b c

a - b = b - c

2b = a+c

b = a+c/2

1 3 5 7 9


First we need to sort
then check if each continious three pair b= a+c/2

----


Probably there is a math solution

a b c 

x a b c y

x + y = 4 * b

it is a series when elem count is even



'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr = sorted(arr)
        
        for i in range(len(arr)-2):
            
            if arr[i] + arr[i+2] != 2*arr[i+1]:
                return False
            
        return True
            
        
        
        