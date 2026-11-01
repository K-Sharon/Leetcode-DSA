class Solution:
    def minMoves(self, nums: list[int]) -> int:
        if len(set(nums))==1:
            return 0
        mn=min(nums)
        res=0
        for i in nums:
            if i==mn: continue
            res+=(i-mn)
        return res
        