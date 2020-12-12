'''
Best Time to Buy and Sell Stock II
<T> Array <T> Greedy

int [] prices
    - ith element is the price of a given stock on day i

Find the maximum profit
    - As many transactions as time
    - Can't do multiple transactions
    - Buy one sell one at a time

Strategy

You get first one as base
    - When dipping -> move base next
    - When starting upward -> Mark that as to sell
        - If starts dipping, sell it


'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # mode 0 -> looking to buy, 1 -> loıoking to sell
        # Simple iteration with state
        mode = 0
        base = None
        sell = None
        profit = 0
        for i in range(len(prices)):
            
            
            # Quick fix for the final elem where there is no trajectory
            if i >= len(prices) - 1:
                if mode == 1:
                    sell = i
                    profit += prices[sell] - prices[base]
            else:
                if mode == 0:
                    base = i
                    # Upward - Change to sell mode
                    if prices[i+1] > prices[i]:
                        sell = i+1 
                        mode = 1
                    # Downward, do not modify
                elif mode == 1:
                    sell = i
                    # Downward, sell it
                    if prices[i+1] <= prices[i]:
                        profit += prices[sell] - prices[base] 
                        mode = 0
                    # Upward, do not modify
                
        return profit