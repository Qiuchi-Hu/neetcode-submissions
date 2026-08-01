class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_in = prices[0]
        sell = prices[0]
        max_profit= 0

        for price in prices:
            if(price>sell):
                sell = price
            elif(price<buy_in):
                buy_in=price
                sell=price
        
            max_profit = max(max_profit, sell-buy_in)
            
        return max_profit
        