class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq=defaultdict(set)
        setNums=set(nums)
        setid=0
        i=0

        while(setid<len(setNums) and i<len(setNums)):
            num=list(setNums)[i]
            seq[setid].add(num)
            if num-1 in setNums:
                seq[setid].add(num-1)
            for j in range(1,len(nums)):
                if num +j  in setNums:
                    seq[setid].add(num + j)
                else:
                    i += j
                    break
            setid += 1
        max=0
        for s in seq.values():
            if(len(s)>max):
                max=len(s)
        return max