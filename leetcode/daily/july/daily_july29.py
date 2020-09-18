'''

obj: Find the maximum profit

constraints
--> 1 transaction one day or skip the day
--> 1 stock limit
    --> S: 0 , either buy or skip
    --> S: 1 , either sell+skip(2days--cooldown) or skip


algorithm
def algo(prices, stock, day):
    
    stock = 0
    day = 1
    if stock == 0:
        # Should buy?
        
        day += 1
    else:
        # Should sell?
        
        if sell:
            day +=1
        day += 1 


# We use an incremental approach to build recursive tree
# We recurse each option, return the leaf score

# If there is a pattern, we can exploit the DP later
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        stock = 0
        day = 0
        profit = 0
        
        self.prices = prices
        
        return self.dfs(stock, day, profit)
        
    def dfs(self, stock, day, profit):
        
        # Base case, end
        if day >= len(self.prices):
            return profit
        
        # Current Price
        price = self.prices[day]
        
        if stock == 0:
            # max(bought, not bought)
            profit = max(self.dfs(1, day+1, profit-price), self.dfs(0, day+1, profit))
        elif stock == 1:
            # max(sold (2 day skip), not sold)
            profit = max(self.dfs(0, day+2, profit+price), self.dfs(1, day+1, profit))
        
        return profit

        