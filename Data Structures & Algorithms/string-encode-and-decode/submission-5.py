

class Solution:
    def encode(self, strs: list[str]) -> str:
        if len(strs)==0:
            return "0null"
        key= str()
        size=len(strs)
        for i in range(size):
            s=strs[i]
            for j in range(len(s)):
                c=s[j]
                key+=(str(ord(c)))#Calculate code for unicode
                if j<len(s)-1:
                    key += "/"

            if i<size-1:
                key += "$"

        return key
    def decode(self, s: str) -> list[str]:
        if s=="0null":
            return []
        encodedList=s.split("$")
        originalList=[]
        for s in encodedList:
            originalString=""
            for c in s.split("/"):
                if c=="":
                    originalString+=""
                else:
                    originalString+=chr(int(c))
            originalList.append(originalString)
        return originalList