class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        best=0
        while r < len(prices):
             if prices[r] > prices[l]:
                best= max(best,prices[r]-prices[l])
                r+=1
             else:
                l=r
                r+=1
        return best
        
        