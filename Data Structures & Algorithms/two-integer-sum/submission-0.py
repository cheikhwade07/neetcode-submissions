class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsindex={}
        for i in range(len(nums)):
            if nums[i] not in numsindex :
                numsindex[nums[i]]=i
            diff = target-nums[i]
            if numsindex.get(diff) !=None and numsindex[diff]!=i:
                return [numsindex[diff],i]
        return [False,False]