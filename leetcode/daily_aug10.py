'''
Excel sheet col number

A - 1
Z - 25 

It is a numbering system on base 27



Constraints
s: str 
1 <= len(s) <= 7
other constraint is arbitrary
'''


class Solution:
    def titleToNumber(self, s: str) -> int:
        
        multiplier = 1
        total_val = 0
        
        for i in range(len(s)-1, -1, -1):
            item = s[i]
            
            item_val = (ord(item) - ord('A') + 1)
            
            if multiplier != 1:
                item_val = item_val * multiplier
                
            total_val += item_val
            #print(item, item_val)
            multiplier = multiplier * 26
        return total_val