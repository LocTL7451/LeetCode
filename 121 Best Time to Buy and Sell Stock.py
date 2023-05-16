# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 1010 ms
Beats | 68.31%
Memory | 27.5 MB
Beats | 5.96%

"""

"""
    The approach here is to keep a rolling maximal value representing the max profit at any given time
    To do this, we apply a shifting window approach, moving left and right pointers along the array until the rightmost pointer
    reaches the end of the array. 
"""
class Solution:
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        priceDiff = 0
        while sell < len(prices):
            currDiff = prices[sell] - prices[buy]
            if prices[sell] > prices[buy]:
                priceDiff = max(priceDiff, currDiff)
            else: 
                buy = sell 
            sell += 1
        return priceDiff
                
        

            
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
                
            
        
    
