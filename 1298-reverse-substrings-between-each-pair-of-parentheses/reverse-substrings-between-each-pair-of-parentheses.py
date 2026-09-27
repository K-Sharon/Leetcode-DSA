class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk=[]
        curr=''
        for c in s:
            if c=='(':
                stk.append(curr)
                curr=''
            elif c==')':
                curr=curr[::-1]
                curr=stk.pop()+curr
            else:
                curr+=c
        return curr