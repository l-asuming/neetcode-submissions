class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        i = 0
        k = len(prices)


        while i+1 < k:
            for j in range(i+1,k):
                profit = max(profit, prices[j] - prices[i])
            i += 1
       
        return profit
