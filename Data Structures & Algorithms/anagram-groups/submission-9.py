class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_s={}
        for s in strs:
            freq={}
            for c in s:
                freq[c] = freq.get(c,0) +1
            dict_s.setdefault(tuple(sorted(freq.items())),[]).append(s)

        return list(dict_s.values())