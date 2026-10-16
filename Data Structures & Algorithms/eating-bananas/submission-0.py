class Solution:
    def minEatingSpeed(self,piles,h):
        low = 1
        high = max(piles)
        k = (high + low  ) // 2

        while (low != high):
            if ( self.test_k(k, piles, h) ):
                high = k
            else:	
                low = k+1
            k = (high + low ) // 2
            
        return k 


    def test_k(self,k,piles,h):
        for p in piles:
            hours_needed = p//k 
            if p % k !=0:
                hours_needed +=1
            h -= hours_needed	
            if ( h < 0 ): 
                return False
        return True
