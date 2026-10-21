class Solution:
    def rob(self, nums: List[int]) -> int:
        value = {}
        def rob(n) -> int:
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[1],nums[0])
                            
            if n in value:
	            return value[n]
            else:
                value[n] = max(rob(n-1),rob(n-2)+nums[n])
                return value[n]
        return rob(len(nums)-1)
       
        