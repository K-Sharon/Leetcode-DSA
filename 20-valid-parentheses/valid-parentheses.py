class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(',']':'[','}':'{'}
        stk=[]
        for c in s:
            if stk and c in dic and dic[c]==stk[-1]:
                stk.pop()
            else:
                stk.append(c)
        if stk:
            return False
        else:
            return True
            