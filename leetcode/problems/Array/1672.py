'''
int [m][n] accounts
- amount of money iyh customer has in the jth bank
- return the wealth that the richest customer has

sum by row, get max

'''

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        most = -1
        for row in accounts:
            total = 0
            for item in row:
                total += item
            
            most = max(total,most)
        
        return most
            
        