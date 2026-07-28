class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            goal=target-nums[i]
            
            if goal in d:
                return [d[goal], i]
            d[nums[i]]=i