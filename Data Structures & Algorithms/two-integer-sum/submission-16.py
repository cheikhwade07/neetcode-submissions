class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}
        for num,i in zip(nums,range(len(nums))):
            diff = target - num
            if diff in prev.keys():
                print(diff)
                return [prev[diff],i]

            prev[num] = i
            print(prev[num])