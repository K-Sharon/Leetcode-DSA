class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        for k in range(1,n+1):
            if n%k!=0:
                continue
            valid=True
            prevmax=float('-inf')
            for start in range(0,n,k):
                mn=float('inf')
                mx=float('-inf')
                des=0
                for j in range(start,start+k):
                    mn=min(mn,nums[j])
                    mx=max(mx,nums[j])
                    if j>start and nums[j-1]>nums[j]:
                        des+=1
                if des>1 or (des==1 and nums[start+k-1]>nums[start]) or prevmax>mn:
                    valid=False
                    break
                prevmax=mx
            
            if valid:
                ans+=k
        return ans


