class Solution:
    def rob(self, nums):
        dp={}
        def top_bottom(n):
            if n == 0:
                return nums[0]
            elif n==1 : 
                return max(nums[0],nums[1])
            if n not in dp : 
                dp[n] = max( top_bottom(n-1) ,top_bottom( n-2) + nums[n] )
            return dp[n]
        return top_bottom(len(nums)-1)