class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberSet={}
        for num in nums:
            if numberSet.__contains__(num) is False:
                numberSet[num]=1
            else:
                return True

        return False
