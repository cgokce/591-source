'''
Using the given hint, thinking about the increasing step size

Constraints
- Either 1 or 2 step
- Steps can interchange(permutation)

Algorithm

def algorithm(n):
    
    # Base case success
    if n == 2:
        return 2 # Two options
    elif n == 1:
        return 1
    elif n == 0:
        return 0
        
    # Recursion, return 1 and 2 step results
    return algorithm(n-1) + algorithm(n-2)

'''


# Vanilla recursion successful but time limit
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Base case success
        if n == 2:
            return 2 # Two options
        elif n == 1:
            return 1
        elif n == 0:
            return 0
        
        # Recursion, return 1 and 2 step results
        return self.climbStairs(n-1) + self.climbStairs(n-2)
'''

# Dynamic Programming, will just add memoization for each step, changed to the bottom up
# It just became the fibonacci sequence

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.dynamic(n)
        
    def dynamic(self, n):
        
        memory = [None for i in range(n+2)]
        
        memory[1] = 1
        memory[2] = 2
        
        for i in range(3,n+1):
            # Either 1 step or 2 step
            memory[i] = memory[i-1] + memory[i-2]

        return memory[n]