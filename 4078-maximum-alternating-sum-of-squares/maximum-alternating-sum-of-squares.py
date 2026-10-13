class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[abs(i) for i in nums]
        nums.sort()
        n=len(nums)
        k=n//2
        arr=[]
        for i,j in zip(nums[:k],nums[k:]):
            arr.extend([j,i])
        if n%2!=0:
            arr.append(nums[-1])
        res=0
        for i in range(n):
            if i%2==0:
                res+=arr[i]**2
            else:
                res-=arr[i]**2
        return res


        