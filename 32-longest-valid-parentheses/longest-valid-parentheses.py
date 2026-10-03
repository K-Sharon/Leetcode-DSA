class Solution:
    def longestValidParentheses(self, s: str) -> int:
        cnt=0
        stk=[-1]
        for i in range(len(s)):
            if s[i]=='(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    cnt=max(cnt,i-stk[-1])
        return cnt

            

