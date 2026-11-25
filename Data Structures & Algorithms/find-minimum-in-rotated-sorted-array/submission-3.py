class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        middle = (l+r)//2
        for _ in range(len(nums)): 
            
            if nums[middle] <= nums[middle-1]:
                return nums[middle]
            middle -=1
        
            
            
        return 1