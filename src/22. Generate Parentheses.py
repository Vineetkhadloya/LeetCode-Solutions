# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        st = []
        res = []
        
        def backTrack(openP,closeP):
            
            if openP == closeP == n :
                res.append("".join(st))
                return
            
            if(openP < n):
                st.append("(")
                backTrack(openP + 1,closeP)
                st.pop()
            
            
            if(closeP < openP):
                st.append(")")
                backTrack(openP,closeP+1)
                st.pop()
        
        backTrack(0,0)
        return res