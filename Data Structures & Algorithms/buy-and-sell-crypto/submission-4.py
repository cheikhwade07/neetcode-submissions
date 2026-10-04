class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        for l in range(len(prices)):
            r=l+1
            while r<len(prices) and prices[r] > prices[l]  :
                profit=prices[r]- prices[l]
                if profit > max:
                    max=profit
                r+=1

        return max
            
            


