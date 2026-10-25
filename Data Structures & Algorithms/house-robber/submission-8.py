class Solution:     
    def rob(self, nums):
        bottom_up = [ 0 for i in range(len(nums)) ]
        for n in range(len(nums)):
            if n == 0:
                bottom_up[0]=nums[0]
            elif n==1 : 
                bottom_up[1] =  max(nums[0],nums[1])
            else:
                bottom_up[n] = max( bottom_up[n-1] , bottom_up[n-2] + nums[n] )
            
        return bottom_up[-1]
            