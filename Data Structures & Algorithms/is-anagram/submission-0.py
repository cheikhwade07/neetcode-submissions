class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        LetterSet1={}
        LetterSet2={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in LetterSet1:
                LetterSet1[s[i]]=1
            else:
                LetterSet1[s[i]]+=1

            if t[i] not in LetterSet2:
                LetterSet2[t[i]]=1
            else:
                LetterSet2[t[i]]+=1
        for char in LetterSet1.keys():
            if char not in LetterSet2:
                return False
            if LetterSet2[char]!=LetterSet1[char]:
                return False

        return True


sol=Solution().isAnagram("jar", "jam")
print(sol)
