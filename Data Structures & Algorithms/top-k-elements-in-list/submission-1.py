class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequence={}
        for num in nums:
            frequence[num]=frequence.get(num,0)+1

        output=sorted(frequence,key=lambda number:frequence[number])

        return output[len(output)-k:len(output)]
