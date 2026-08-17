class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #The current max profit
        max_profit = 0
        #The least price seen so far
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            #end if
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit