class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:
            return ""
        if sum==0:
            return '0'
        
        res=""
        for i in range(num):
            if sum>9:
                res+='9'
                sum-=9
            else:
                res+=str(sum)
                sum=0
        return res
