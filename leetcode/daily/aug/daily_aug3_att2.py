'''
Valid Palindrome - Attempt#2

Constraints
--> Non-alphanumerics doesn't count
--> Time constraint, no unnecessary recursion
--> Still max O(n) only single iteration of the whole array
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Get rid of non-alphanumericals
        # Needs memory but might save few ops
        
        trimmed = ""
        
        for c in s:
            if c.isalnum():
                trimmed += c
        
        # Convert the single case for the comparison
        trimmed = trimmed.lower()
        
        # Two pointer approach
        i = 0
        j = len(trimmed) -1
        
        while(i<=j):
            if (trimmed[i] != trimmed[j]):
                return False
            i += 1
            j -= 1
        
        return True
        
        
        
        
        
        
        