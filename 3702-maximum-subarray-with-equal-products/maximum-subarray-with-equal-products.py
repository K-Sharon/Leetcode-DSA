class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        mx=0
        for i in range(n):
            p,l,h=nums[i],nums[i],nums[i]
            for j in range(i+1,n):
                p*=nums[j]
                l=math.lcm(l,nums[j])
                h=math.gcd(h,nums[j])
                if p==l*h:
                    mx=max(mx,j-i+1)
        return mx


