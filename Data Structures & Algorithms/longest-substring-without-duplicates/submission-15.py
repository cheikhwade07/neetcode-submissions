class Solution:
    def lengthOfLongestSubstring(self, s: str):
        d={}
        l=0
        seq=0
        for r in range(len(s)):
            if s[r] in d:
                l=max(l,d[s[r]]+1)
            d[s[r]]=r
            seq=max(r-l+1,seq)
        return seq