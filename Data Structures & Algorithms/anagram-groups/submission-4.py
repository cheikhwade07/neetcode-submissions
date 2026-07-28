class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in range(len(strs)) :
            w="".join(sorted(strs[i]))
            d[w].append(strs[i])
         
        return list(d.values())