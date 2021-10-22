# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Handling edge case
        if(len(prices)<=1): return 0
        
        maxProfit = 0
        
        l = 0
        r = 1
        
        while r < len(prices):
            
            # if price of value of left right pointer is less than that at right we calculate profit
            # Else left pointer will move to position of right
            if(prices[l] < prices[r]):
                maxProfit = max(maxProfit,prices[r]-prices[l])
            else :
                l = r

            # In both case right pointer will be increased by 1
            r += 1
            
        return maxProfit