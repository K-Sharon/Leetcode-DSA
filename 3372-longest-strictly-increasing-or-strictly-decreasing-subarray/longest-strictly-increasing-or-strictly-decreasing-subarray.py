class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        mx=1
        c=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                c+=1
                mx=max(mx,c)
            else:
                c=1
        c=1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c+=1
                mx=max(mx,c)
            else:
                c=1
        return mx
        