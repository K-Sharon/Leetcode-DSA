class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        memo=[[None]*(n+1) for i in range(n)]
        def check(i,b):
            if b<0:
                return False
            if i==n:
                return b==0
            if memo[i][b] is not None:
                return memo[i][b]
            if s[i]=='(':
                res = check(i+1,b+1)
            elif s[i]==')':
                res = check(i+1,b-1)
            else:
                res = check(i+1,b+1) or check(i+1,b-1) or check(i+1,b)     
            memo[i][b]=res
            return res      
        return check(0,0)
                        