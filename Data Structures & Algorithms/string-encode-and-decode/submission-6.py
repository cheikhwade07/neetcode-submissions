
class Solution:
    def encode(self, strs: list[str]) -> str:
        key= ""
        size=len(strs)
        for s in strs:
            key += str(len(s))
            key += "#"
            key += s

        return key
    def decode(self, s: str) -> list[str]:
        originalList=[]
        i = 0
        sizeS=len(s)
        while i<sizeS:
            size = ""
            next = s[i]
            while next!="#" :
                size += next
                i += 1
                next = s[i]
            i+=1
            size = int(size)
            word = s[i:i+size]
            i+=size
            originalList.append(word)

        return originalList


