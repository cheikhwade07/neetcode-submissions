class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numsindex = {}
        for i in range(len(numbers)):
            if numbers[i] not in numsindex:
                numsindex[numbers[i]] = i
            diff = target - numbers[i]
            if numsindex.get(diff) != None and numsindex[diff] != i:
                return [numsindex[diff]+1, i+1]