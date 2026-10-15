class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        longest=0
        l=0
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            while (k < (r-l+1) - max(freq.values())) : #check for invalid window
                #shrinking
                freq[s[l]] -= 1
                l+=1
            longest = max(longest, r-l+1)
        return longest
