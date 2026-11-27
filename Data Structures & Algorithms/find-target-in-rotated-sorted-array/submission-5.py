class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l= 0 
        r = len(nums) - 1
        
        while l < r: 
            middle = (r+l)// 2 
            if nums[middle] < nums[r]:
                r = middle 
            else: 
                l = middle + 1
        pivot = l 
        r = len(nums) - 1

        def binary_search(l,r):
            while l <= r: 
                middle = (l+r)//2
                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    r = middle - 1 
                else: 
                    l = middle + 1 
            return - 1
        
        if not nums[pivot] <= target <= nums[r]: 
            l = 0 
            r = pivot - 1
        
            
        
            
        return binary_search(l,r)
