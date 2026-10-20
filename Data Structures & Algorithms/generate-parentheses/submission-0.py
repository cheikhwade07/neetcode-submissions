class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        remaining_open = n
        remaining_close = n
        
        def generate_parenthesis(strs,remaining_open,remaining_close):
            if remaining_close < remaining_open:
                    return 
            if remaining_open ==0 and remaining_close == 0:
              
                out.append(strs)
            alt=strs
            if remaining_open > 0:
                strs += "("
                generate_parenthesis(strs, remaining_open-1,remaining_close)
  
   
            if remaining_close >0:
                alt += ")"
                generate_parenthesis(alt,remaining_open,remaining_close-1)
            

        generate_parenthesis("(",remaining_open-1,remaining_close)
        return out


'''       
Input: n = 1

Output: ["()"]
        
        
 Input: n = 2

Output: ["(()),()()"]
               
n_closing_parenthesis >=n_opening_parenthesis
remaining_open_parenthesi = 0
remaining_close_parenthesi = 2
if remaining_close_parenthsis < remainin_open_par:
        Invalid
if remaininng_open and remaining_close == 0:
    out.append(strs)
    return 
'''
