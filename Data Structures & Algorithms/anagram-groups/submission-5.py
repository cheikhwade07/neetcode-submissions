class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = strs[:]
        
        for i in range(len(strs)):
             sorted_strs[i] = "".join(sorted(sorted_strs[i]))
        
        out = {}    
       
        for i in range(len(strs)):
            out.setdefault(sorted_strs[i], []).append(strs[i])
            print(strs[i])

       
        return list(out.values())
            
            
        
