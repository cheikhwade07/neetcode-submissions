class Solution:
    def check(self, nums: List[int]) -> bool:
        ans = 0
        for i in range(len(nums)): 
            if nums[i] < nums[i-1]: 
                ans +=1 
        print(ans)
        return ans <= 1 