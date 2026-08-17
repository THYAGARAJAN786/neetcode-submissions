class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        #Brute force
        for initial_index in range(len(prices)):
            for final_index in range(initial_index + 1, len(prices)):
                max_profit = max(max_profit, prices[final_index] - prices[initial_index])
            #end for
        #end for
        return max_profit