class Solution:
    def isValid(self,s : str):
        corresponding = {
        ")" : "(" ,
        "}" : "{",
        "]":"["
        }
        open_parenthesis = []
        for c in s: 
            if c not in corresponding :
                open_parenthesis.append(c)
                continue
            if open_parenthesis and corresponding[c] == open_parenthesis[-1]:
                open_parenthesis.pop()
                continue
            return False
        return not open_parenthesis

        