class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod=10**9+7
        def helper(nums):
            n=len(nums)
            if n<3:
                return 1
            left=[i for i in nums if i<nums[0]]
            right=[i for i in nums if i>nums[0]]
            return helper(left)*helper(right)*comb(n-1,len(left))%mod
        return(helper(nums)-1)%mod

        