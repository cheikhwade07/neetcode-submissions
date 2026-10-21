class Solution:
    def rob(self, nums: List[int]) -> int:
        value = [0]*len(nums)
        def rob(n) -> int:
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[1],nums[0])
                            
            if value[n] != 0:
	            return value[n]
            else:
                value[n] = max(rob(n-1),rob(n-2)+nums[n])
                return value[n]
        return rob(len(nums)-1)
       
        