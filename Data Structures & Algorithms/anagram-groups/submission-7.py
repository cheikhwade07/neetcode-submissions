class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_s={}
        for s in strs:
            key="".join(sorted(s))
            dict_s.setdefault(key,[]).append(s)

        return list(dict_s.values())