class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_n={}

        for num in nums:
            dict_n[num]= dict_n.get(num,0)+1
            if dict_n[num] >=2:
                return True
        return False