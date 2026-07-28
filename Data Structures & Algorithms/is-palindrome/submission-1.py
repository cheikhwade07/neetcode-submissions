class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=""
        s=s.replace(" ", "").lower()
        for c in s:
            if((ord(c)  in range(ord('a'),ord('z')))or (ord(c) in range(ord("0"),ord("9")))):
                str +=c
        inverseString=str[::-1]
        return inverseString == str

