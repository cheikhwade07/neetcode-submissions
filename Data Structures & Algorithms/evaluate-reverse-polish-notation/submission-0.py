class Solution:
    def evalRPN(self, tokesn: List[str]) -> int : 
        opperations  = {
                "+" : lambda a,b: a + b ,
                "-" : lambda a,b: a - b ,
                "*" : lambda a,b: a * b ,
                "/" : lambda a,b: int(a / b)
             }
        result = []
        for element in tokesn : 
            if element not in opperations : 
                result.append(int(element))
                continue
            right = result.pop()
            left = result.pop()
            calculation = opperations[element](left,right) 
            result.append(calculation)
        return result[-1]
          