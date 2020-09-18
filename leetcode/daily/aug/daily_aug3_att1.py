'''

Valid Palindrome

Constraints
--> Don't consider the non-alphanumeric characters
--> Input contains only printable ASCII characters
--> Case does not matter
    --> Convert all to lowercase or uppercase to compare
--> Empty string does count as palindrome for this problem


def algorithm(self, s):
    
    prev = True
    return self.dfs(prev, s)
    
    
def isValidChar(self, c):
    # Check if the char is valid alphanumerical
    # Also delete space
    pass
    
def compareLowercase(self, c1, c2):
    # Compare given two alphanumerical characters
    # If characters are alphabethicals turn them to lowercase
    # Then compare equality
    pass
    
def dfs(self, prev, s):
    if s = "":
        return True
    
    # Take one from front and back until we get a valid one
    i = 0
    valid = isValidChar(s[0])
    while not valid:
        i += 1
        valid = isValidChar(s[i])
    
    # End case, not a single valid char remaining in the set
    if not valid:
        return prev
    
    # Reverse find valid
    j = -1
    valid = isValidChar(s[j])
    while not valid:
        j -= 1
        valid = isValidChar(s[j])

    if compare_lowercase(s[i],s[j]):
        return True
    else
        return False

    
    
# Take 1 from forward, 1 from backward
# We can do a recursive action, by trimming palindrome after each match

ab.c: cba 

front a
back a
a == a
return(b.c: cb)

front b
back b
return .c: c

front . --> not valid resample
front c
back c
return ": "

front :
front _
return prev_result.



'''

# 480/481 - Time Limit on the last case,
# need a better solution
# This is O(n), just processes the each element once
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #s = ".,"
        #s = "race a car"
        #s = "1a2"
        return self.dfs(s)


    def lc(self, c):
        # Lowercase a character if only it is a number
        #print(c)
        if c.isalpha():
            return c.lower()
        else:
            return c
        
    # Prev here looks like useless, we'll see
    def dfs(self, s):
        
        # Base case: Empty or have size of one
        if (s == "") or (len(s) == 1):
            return True        
        
        #print(s)
        #print(len(s))
        
        
        # Take one from front and back until we get a valid one
        i = 0
        valid = s[i].isalnum()
        
        while (not valid) and (i<len(s)-1):
            i += 1
            valid = s[i].isalnum()

        # End case, not a single valid char remaining in the set
        if i+1 == len(s):
            return True

        # Reverse find valid
        j = -1
        valid = s[j].isalnum()
        while not valid:
            j -= 1
            valid = s[j].isalnum()

        if self.lc(s[i]) == self.lc(s[j]):
            #print("true")
            #print(i,j)
            return self.dfs(s[i+1:j])
        else:
            #print("false")
            return False
        