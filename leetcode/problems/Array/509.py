'''
Fibonacci Number
<T> Array

Given N, calc Fibonacci(N)
'''


class Solution:
    def fib(self, N: int) -> int:
        
        if N == 0:
            return 0
        elif N == 1:
            return 1
        
        
        seq = [0, 1]
        
        for i in range(2, N+1):
            seq.append(seq[i-1] + seq[i-2])
            
        
        
        print(seq)
        return seq[-1]