class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        prevs=self.prevProduct(nums)
        subs=self.subsProduct(nums)
        out=[]
        for i in range(size):
            out.append(prevs[i]*subs[i])
        return out
    def prevProduct(self,nums)->List[int]:
        size=len(nums)
        prev=[0]*size
        for i in range(size):
            if i==0:
                prev[i]=1
            else:
                product=prev[i-1]*nums[i-1]
                prev[i]=product
        return prev

    def subsProduct(self, nums) -> List[int]:
        size = len(nums)
        subs = [0]*size
        for i in range(size-1,-1,-1):
            if i == size-1:
                subs[i] = 1
            else:
                product = subs[i + 1] * nums[i+1]
                subs[i] = product
        return subs
