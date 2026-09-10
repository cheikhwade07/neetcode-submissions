class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMaps = {}

        for i in range(len(nums)):
            
            x = target - nums[i]
            if x in numMaps:
                return [numMaps[x], i]
            numMaps[nums[i]] = i
