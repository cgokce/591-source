'''
num: int32 
check if power of 4.
num =? 4*4*...
recursion
--> exception 1 is still power of 4

'''



class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        return self.dfs(1, num)
        
    def dfs(self, curr, num):
        
        if curr == num:
            return True
        elif curr>num:
            return False
        
        
        return self.dfs(curr*4, num)
        