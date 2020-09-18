'''
Best Time to Buy and Sell Stock III
<T> Array       <T> Dynamic Programming


Addition upon previous:
    Max transactions are 2
    

So this needs a whole traversal and planning
# Premise only 2 transactions
# Only 1 buy 1 sell allowed means 2 subarrays
# DP calculate left and right subarrays
# DP max(curr, next)

forward pass keeps min
bw pass keeps max

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #Base case
        if len(prices) <= 1:
            return 0
        
        l = prices[0]
        r = prices[len(prices)-1]
        
        # Init left and right subarrays
        left_sub = [0 for i in range(len(prices))]
        right_sub = left_sub[:]
        
        #direct traverse O(N)
        for i in range(1, len(prices)):
            
            # Reverse pointer
            rev = len(prices) - 1 - i
            
            # update left sub
            left_sub[i] = max(left_sub[i-1], prices[i] - l)
            # update min price
            l = min(l, prices[i])
            
            # update right sub, same thing
            right_sub[rev] = max(right_sub[rev+1], r - prices[rev])
            # update min price
            r = max(r, prices[rev])
            
        # Calculation done
        # Find the best sum, O(n)
        score = left_sub[0] + right_sub[0]
        
        #right_sub.append(-999)
        for i in range(len(left_sub)):
            # update if better score exists
            if score <= (left_sub[i] + right_sub[i]):
                score = left_sub[i] + right_sub[i]
                
        #print(left_sub)
        #print(right_sub)
        
        return score
        
        
        