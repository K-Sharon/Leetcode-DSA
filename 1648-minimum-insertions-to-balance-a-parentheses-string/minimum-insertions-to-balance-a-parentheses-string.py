class Solution:
    def minInsertions(self, s: str) -> int:
        left,right,i=0,0,0
        while i<len(s):
            if s[i]=='(':
                left+=1
            else:
                if i+1<len(s) and s[i+1]==')':
                    i+=1
                else:
                    right+=1
                if left>0:
                    left-=1
                else:
                    right+=1
            i+=1
        return right+left*2
        
   