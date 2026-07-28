class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ", "").lower()
        str=""
        for c in s:
            if((ord(c)  in range(ord('a'),ord('z')+1)) or (ord(c) in range(ord('0'),ord('9')+1))):
                str +=c
        l = 0
        r = len(str) - 1
        for i in range(len(str)):
            ls=str[l + i]
            rs=str[r - i]
            if(ls!=rs):
                return False
        return True
