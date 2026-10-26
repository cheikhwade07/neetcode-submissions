class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
       
        dp ={}
        def coin_amount_to( value : int)->int : 
            if value == 0:
                return 0
            valid_coin =[]
            #ignore invalid coin
            #dfs on valid_coin
            min_coin = float('inf')
            for c in coins : 
                remaining = value-c
                if remaining >= 0:
                    if remaining not in dp:
                        dp[remaining] = coin_amount_to(remaining) 
                    min_coin = min(min_coin, dp[remaining] +1)
           
       
            return min_coin
                
        min_coin= coin_amount_to(amount)
        if min_coin == float('inf'):
            return -1 
        return min_coin

        