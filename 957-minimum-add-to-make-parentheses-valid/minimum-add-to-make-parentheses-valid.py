class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk=[]
        for c in s:
            if c==')':
                if stk and stk[-1]=='(':
                    stk.pop()
                else:
                    stk.append(c) 
            else:
                stk.append(c)
        return len(stk)
