class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res=[]
        for i in range(m):
            if i==0:
                val='.'*n
            else:
                val='#'*(n-1)+'.'
            res.append(val)
        return res
                