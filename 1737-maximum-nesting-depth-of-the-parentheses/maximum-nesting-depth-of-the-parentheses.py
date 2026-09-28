class Solution:
    def maxDepth(self, s: str) -> int:
        stk=[]
        mx=0
        for i in s:
            if i=='(':
                stk.append(i)
            elif i==')' and stk:
                stk.pop()
            mx=max(mx,len(stk))
        return mx
            