class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        r=10
        while r>0:
            n=n-r
            r-=1
            if r>n:
                return r%2!=0
        return False
