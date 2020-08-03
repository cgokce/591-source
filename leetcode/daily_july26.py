'''

Add Digits

given num:int

add all digits iteratively until no digit left

Naive approach: Recursion, loop

38
3+8 = 11
1+1 = 11

def algo(num):
    return self.dfs(num)
    

def dfs(self, num):
    
    # Base case
    if num<10:
        return num
    
    sum = 0
    while num>9:
        sum += num%10
        num = num/10

    sum+=num
    return sum
        


'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.dfs(num)
    

    def dfs(self, num):

        # Base case
        if num<10:
            return num

        sum = 0
        while num>9:
            sum += num%10
            num = num/10

        sum+=num
        
        # Recursion
        return self.dfs(sum)
