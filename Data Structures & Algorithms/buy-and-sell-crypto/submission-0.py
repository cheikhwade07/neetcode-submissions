class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=[]
        for i in range(len(prices)-1):
             max_profit= max(prices[i:])
             if max_profit > prices[i]:
                best.append(max_profit-prices[i])
        if len(best) == 0:
            return 0
        return max(best)
        
        