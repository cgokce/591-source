'''
Final Prices With a Special Discount in a Shop
<T> Array

Given:
int [] prices
- Prices[i] is the price of the ith item in shop
- Special discount for items in the shop if you buy ith item
    - Then you will receive discount as prices[j]
        - j is minimum index j>i and prices[j] <= prices[i]
        - If not exists, no discount at all
    - Return an array where ith element is the final price you will pay for the ith item
    
    
Approach:
- Brute force, just calculate one by one
    - O(n^2) time
    - O(n) space

- Should be a bit faster, keep the previous states in a backlog array, calculate discount when applicable
    - This is also kind of exhausing
    - Might be easier when we also keep a sorted backlog
    - This is also iterating backlog every time, so still a slow one

'''

class Solution:
    # Simple Brute Force
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        ret = prices.copy()
        
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    ret[i] = prices[i] - prices[j]
                    break
        
        return ret
        
    '''
    - Failed indexing with hmap
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        ret = [None for i in range(len(prices))]
        hmap = {}
        
        for i in range(len(prices)):
            
            item = prices[i]
            hmap[i] = item
            
            print(i, item)
            print("----")
            
            hmap2 = hmap.copy()
            
            print(hmap2.keys())
            for key in hmap2.keys():
                if key >= i:
                    continue
                
                back = hmap[key]
                if item <= back:
                    ret[key] = back-item
                    hmap.pop(key)
                    break
                    
            print("################")

    
        for key in hmap.keys():
            ret[key] = item
            
        return ret
    '''