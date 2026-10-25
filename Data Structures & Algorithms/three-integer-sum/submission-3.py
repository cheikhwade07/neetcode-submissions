class Solution:
    def threeSum(self,nums) : 
        index={}
        out=[]
        size= len(nums)
        for i in range( size ) :
            index.setdefault(nums[i],[]).append(i)

        for i in range( size ):
            for j in range(i+1, size ):
                comb = nums[ i ] + nums[ j ]
                diff = 0 - comb
                if diff not in index:
                    continue
                for z in index[diff]:
                    if z != i and z != j:
                        arr = [ nums[i], nums[j] , nums[z] ]
                        arr.sort()
                        if arr not in out:
                            out.append(arr)
                        break
                           
        return out

        