'''
Best Time to Buy and Sell Stock
<T> Array <T> Dynamic Programming


Given: arr<prices>
    i'th element is the price of given stock on day i

Constraints
    - One transaction total
    - Design an algorithm to find max profit
    - Can't sell stock until you buy one

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curr_min = 9999
        profit = 0
        
        for item in prices:
            # compute the current profit
            profit = max(profit, item - curr_min)
            
            # update the minimum so far
            if item < curr_min:
                curr_min = item
                
        return profit