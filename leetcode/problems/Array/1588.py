'''
Sum of All Odd Length Subarrays
<T> Array

Calculate the sum of all possible odd-length subarrays

Return the sum of all odd-length subarrays

-----------------

Trying to come up with the math solution
a  = a
ab = a + b
abc = a + b + c + [abc] = 2 * (a + b + c)
abcd = 2 * (a+b+c+d)
abcde = [1](a+b+c+d+e) + [3]2*(a+b+c+d+e) + [5]a+b+c+d+e = 4 * a + b + c + d + e
abcdef = [1] SUM + [3] 2*SUM + [5] SUM  = 4*SUM

N items, with sum of S
repeat N/2 Times => 1*S + 2*S + 1*S + 2*S ..... 

-----------------

Question is only interested in contigious subarrays! New formula

a = SUM
ab = SUM
abc = SUM + abc SUM
abcd = SUM + abc bcd (1221)
abcde = 11111 + abc bcd cde 12321 + abcde 11111
abcdef = 11111 + abc bcd cde def 123321 + abcde bcdef 12221

there is a binomial like pattern, but cannot figure out atm, will go with brute force.

------------------

Brute force solution, its viable since arr length <100

get sum
len(arr) = N

for i in range(len(arr)):
    for subcount in range(1,len(n+1)+1,2):

        i to i+subcount
        for(j=i;j<i+n;j++):
        

        1 2 3 4 5 6 7
        123 234 345





'''
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        result = 0
        
        for i in range(n):
            for subcount in range(1, n+1, 2):
                
                if i+subcount<=n:
                    curr_sum = sum(arr[i:i+subcount])
                    result += curr_sum
                    #print(i, subcount, curr_sum)
            
        return result
                
                
                
        
        
        
        