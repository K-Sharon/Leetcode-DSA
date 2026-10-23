class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        sort=sorted(nums)
        rep=[]
        for i in range(len(nums)):
            if sort[i]!=nums[i]:
                rep.append(nums[i])
        if not rep:
            return 0
        res=rep[0]
        for i in range(1,len(rep)):
            res=res&rep[i]
        return res