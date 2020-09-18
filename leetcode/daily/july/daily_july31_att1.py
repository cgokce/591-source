'''
Constraints
--> Given n steps
    ---> 1 step move
    ---> 2 step move
--> Its the permutation, so both (2,1) and (1,2) is possible


Sample case
2
-> 1 + 1
-> 2

3 
-> 1 + 1 + 1
-> 2 + 1
-> 1 + 2

Algorithm
def algorithm(n):
    # Each 3 has 2+1, 1+2, 1+1+1 options
    # Remaining 2 has to 1+1
    # Remaining 1 has to 1
    
    #count = n/3
    #remainder = n%3
    
    # We can recursively apply those
    
    final_list = []
    
    return dfs(n, final_list)
    
    
    
def dfs(n, final_list):

    # Base case Success
    if n==2:
        return "+ 1 + 1"
    elif n==1:
        return "+ 1"
    elif n==0:
        return ""

    # Recursion
    if n>3:
        final_list.append("1 + 1 + 1" + dfs(n%3))
        final_list.append("2 + 1" + dfs(n%3))
        final_list.append("1 + 2" + dfs(n%3))

    # End case
    return final_list


'''

''' Update, its actually sliding window question'''
''' Slide the 3*n part to get different outputs'''

''' Plus keep the strings for the counting different outputs'''
''' Convert the final list into a set for dupe elimination '''



class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prefix = ""
        out_list = self.dfs(prefix, n)
        return  len(set(out_list))
    
    def dfs(self, prefix, n):

        out_score = 0
        out_list = []
        
        # Base case Success
        if n==2:
            return [prefix + "11", prefix + "21"]
        elif n==1:
            return [prefix + "1"]
        elif n==0:
            return 0

        # Recursion
        if n>=3:
            
            remainder = n%3 # 0 or 1 or 2
            # 0| 0 dfs(n)
            # 1| 1 + dfs(n)  ---  dfs(n) + 1
            # 2| 2 + dfs(n)  ---  dfs(n) + 2 
            division = n/3
            
            '''
            # At start
            dfs(division) + others
            
            if n<6
            others + dfs(division)
            '''
            
            
            # Concat Later
            out_list.extend(self.dfs(prefix + "111", division))
            out_list.extend(self.dfs(prefix + "21", division)) 
            out_list.extend(self.dfs(prefix + "12", division)) 
            
            if n<6:
                out_list.extend(self.dfs("111"+ prefix, division))
                out_list.extend(self.dfs("21" + prefix, division))
                out_list.extend(self.dfs("12" + prefix, division))
            
        # End case
        return out_list

        
        
        
