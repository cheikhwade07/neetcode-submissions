class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs= list(strs)
        for i in range(len(strs)):
            sorted_strs[i]= "".join(sorted(sorted_strs[i]))


        dict_s={}
        for s,og in zip(sorted_strs,strs):
            dict_s.setdefault(s,[]).append(og)

        return list(dict_s.values())