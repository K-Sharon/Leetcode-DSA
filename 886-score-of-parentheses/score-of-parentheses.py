class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        dept=0
        score=0
        for i in range(len(s)):
            if s[i]=='(':
                dept+=1
            else:
                if s[i-1]=='(':
                    score+=pow(2,dept-1)
                dept-=1
        return score
