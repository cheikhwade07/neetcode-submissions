

#optimal solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1

            set[tuple(count)].append(s)

        return list(set.values())
strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


