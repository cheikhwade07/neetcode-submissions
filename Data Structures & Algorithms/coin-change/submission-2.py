class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
       
        dp ={}
        def coin_amount_to( value : int)->int : 
            if value == 0:
                return 0
            valid_coin =[]
            #ignore invalid coin
            for c in coins : 
                remaining = value-c
                if remaining >= 0:
                    valid_coin.append(remaining)
            #dfs on valid_coin
            min_coin = float('inf')
            for v in valid_coin:
                if v not in dp : 
                    dp[v] = coin_amount_to(v) 
                min_coin= min( min_coin, dp[v]+1 )

            return min_coin
                
        min_coin= coin_amount_to(amount)
        if min_coin == float('inf'):
            return -1 
        return min_coin

        