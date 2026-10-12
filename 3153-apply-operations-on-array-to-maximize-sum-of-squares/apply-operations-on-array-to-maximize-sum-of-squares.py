class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        arr=[0]*30
        for n in nums:
            for i in range(30):
                arr[i]+= (n>>i) & 1
        res=0
        for j in range(k):
            n=0
            for i in range(30):
                if arr[i]:
                    n |= 1<<i
                    arr[i]-=1
            res=(res+n**2)%(10**9+7)
        return res